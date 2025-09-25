MITM ARP-Spoofing Skript

Ein einfaches Python-Skript zur Durchführung eines Man-in-the-Middle (MITM)-Angriffs mittels ARP-Spoofing. Es nutzt Scapy, um ARP-Tabellen von Zielgerät und Gateway zu manipulieren, sodass der Netzwerkverkehr über die Angreifermaschine geleitet wird. Nur für Lernzwecke in kontrollierten Umgebungen wie TryHackMe verwenden!


Voraussetzungen

•  Python 3 und Scapy (pip install scapy)

•  Root-Rechte (sudo)

•  Netzwerkzugriff auf Ziel-IP und Gateway-IP

•  IP-Forwarding aktiviert: echo 1 > /proc/sys/net/ipv4/ip_forward

•  Tools wie Wireshark oder tcpdump zum Sniffen des Traffic (optional)
Installation


1.  Installiere Scapy, falls nicht vorhanden:

pip install scapy



2.  Speichere das Skript als mitm_arp_spoof.py


Nutzung
1.  Ermittle die IP-Adressen:
	•  Ziel-IP: IP des Opfers (z. B. 10.10.10.5)
	•  Gateway-IP: IP des Routers (z. B. 10.10.10.1)
	•  Finde diese mit ip route (Gateway) oder durch Scannen (z. B. nmap)


2.  Starte das Skript als Root:
sudo python3 mitm_arp_spoof.py <Ziel-IP> <Gateway-IP>


Beispiel:
sudo python3 mitm_arp_spoof.py 10.10.10.5 10.10.10.1


3.  Sniffe den Traffic parallel 
sudo tcpdump -i eth0 -w capture.pcap
oder starte Wireshark.


4.  Beende das Skript mit Ctrl+C. Es setzt die ARP-Tabellen automatisch zurück.



Funktionsweise

•  ARP-Spoofing: Das Skript sendet gefälschte ARP-Pakete, um Zielgerät und Gateway zu täuschen, sodass sie die Angreifermaschine als Gegenstelle sehen.

•  Traffic-Weiterleitung: Mit aktiviertem IP-Forwarding wird der Traffic durchgeleitet, um den Angriff unauffällig zu halten.

•  Rücksetzen: Beim Beenden werden die ARP-Tabellen der Geräte wiederhergestellt.


Hinweise

•  TryHackMe: Perfekt für Rooms wie “Common Attacks” oder “Protocols and Servers 2”. Analysiere gesniffte Pakete, um Flags oder Passwörter zu finden.

•  Fehlerbehebung:
	•  Stelle sicher, dass Scapy korrekt installiert ist.
	•  Überprüfe, ob IP-Forwarding aktiviert ist.
	•  Nutze das richtige Netzwerkinterface (z. B. eth0).

•  HTTPS-Traffic: Für verschlüsselten Traffic sind Tools wie SSLstrip oder Bettercap nötig (nicht enthalten).

Warnung

Dieses Skript ist ausschließlich für ethische Hacking-Übungen in autorisierten Umgebungen gedacht. Die Nutzung in echten Netzwerken ohne Erlaubnis ist illegal und kann rechtliche Konsequenzen haben.


# Lizenz

Dieses Skript wird ohne Gewähr bereitgestellt. Nutzung auf eigene Verantwortung.
