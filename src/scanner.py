from scapy.all import *

eth = Ether(dst="ff:ff:ff:ff:ff:ff")
arp = ARP(pdst="198.13.0.0/24")

a, u = srp(eth/arp)

for i in a:
    print(i[1].psrc + " -- " + i[1].hwsrc)