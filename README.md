# MITM ARP-Spoofing Skript

Ein einfaches Python-Skript zur Durchführung eines **Man-in-the-Middle (MITM)**-Angriffs mittels ARP-Spoofing. Es nutzt [Scapy](https://scapy.net/), um ARP-Tabellen von Zielgerät und Gateway zu manipulieren, sodass der Netzwerkverkehr über die Angreifermaschine geleitet wird. 

> **Warnung**: Nur für Lernzwecke in kontrollierten Umgebungen wie [TryHackMe](https://tryhackme.com/) verwenden! Die Nutzung in echten Netzwerken ohne Erlaubnis ist illegal.


## Voraussetzungen

- **Python 3** und **Scapy** (`pip install scapy`)
- Root-Rechte (`sudo`)
- Netzwerkzugriff auf Ziel-IP und Gateway-IP
- IP-Forwarding aktiviert:
      echo 1 > /proc/sys/net/ipv4/ip_forward

	•  Tools wie Wireshark oder tcpdump zum Sniffen des Traffic (optional)


## Installation

1.  Installiere Scapy:

`pip install -r requirements.txt`

(Siehe requirements.txt für Details.)


2. Speichere das Skript als mitm_arp_spoof.py


## Nutzung

1.  Ermittle die IP-Adressen:
	•  Ziel-IP: IP des Opfers (z. B. 10.10.10.5)
	•  Gateway-IP: IP des Routers (z. B. 10.10.10.1)
	•  Finde diese mit ip route (Gateway) oder durch Scannen (z. B. nmap)


2. Starte das Skript als root

`sudo python3 mitm_arp_spoof.py <Ziel-IP> <Gateway-IP`


Beispiel:

`sudo python3 mitm_arp_spoof.py 10.10.10.5 10.10.10.1`

  
3.  Sniffe den Traffic parallel

`sudo tcpdump -i eth0 -w capture.pcap`
- oder benutze Wireshark


5.  Beende das Skript mit Ctrl+C. 
   	  Es setzt die ARP-Tabellen automatisch zurück.


## Funktionsweise

•  ARP-Spoofing: Sendet gefälschte ARP-Pakete, um Zielgerät und Gateway zu täuschen, sodass sie die Angreifermaschine als Gegenstelle sehen.

•  Traffic-Weiterleitung: Mit aktiviertem IP-Forwarding wird der Traffic durchgeleitet, um den Angriff unauffällig zu halten.

•  Rücksetzen: Beim Beenden werden die ARP-Tabellen der Geräte wiederhergestellt.


## TryHackMe-Tipps

•  Perfekt für Rooms wie Common Attacks oder Protocols and Servers 2.

•  Analysiere gesniffte Pakete (z. B. mit Wireshark), um Flags oder Passwörter zu finden.

•  Für HTTPS-Traffic könnten Tools wie SSLstrip oder Bettercap nötig sein (nicht enthalten).


## Fehlerbehebung

•  Stelle sicher, dass Scapy korrekt installiert ist (pip show scapy).

•  Überprüfe, ob IP-Forwarding aktiviert ist.

•  Nutze das richtige Netzwerkinterface (z. B. eth0).

•  Falls MAC-Adressen nicht gefunden werden, überprüfe die Netzwerkkonfiguration.


## Warnung
Dieses Skript ist ausschließlich für ethische Hacking-Übungen in autorisierten Umgebungen gedacht. 
Die Nutzung in echten Netzwerken ohne Erlaubnis ist illegal und kann rechtliche Konsequenzen haben.


## Lizenz
Dieses Skript wird ohne Gewähr bereitgestellt. 
Nutzung auf eigene Verantwortung.


## Kontakt
Bei Fragen oder Problemen, erstelle ein Issue auf GitHub oder kontaktiere mich in der TryHackMe-Community!




