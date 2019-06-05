# inainte de toate trebuie adaugata o regula de ignorare 
# a pachetelor RST pe care ni le livreaza kernelul automat
# iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
from scapy.all import *
import struct
optiune = 'MSS'
op_index = TCPOptions[1][optiune]
op_format = TCPOptions[0][op_index]
# optiunea MSS are o dimensiune de 2 bytes ('!H')
# ('MSS', '!H')
valoare = struct.pack(op_format[1], 2)
# valoarea 2 a fost impachetata intr-un string de 2 bytes

ip = IP()
ip.src = '172.111.0.14'
ip.dst = '198.13.0.14'

tcp = TCP()
tcp.sport = 54321
tcp.dport = 10000
tcp.option = [(optiune, valoare)]
tcp.seq = 100
tcp.flags = 'S' # flag de SYN
SYN = ip / tcp
raspuns_syn_ack = sr1(SYN)
tcp.seq += 1
tcp.ack = raspuns_syn_ack.seq
tcp.flags = 'A'
ACK = ip / tcp
send(ACK)

for ch in "sal":
    tcp.ack = tcp.seq + 1
    tcp.seq += 1
    tcp.flags = 'PA'
    rcv = sr1(ip/tcp/ch)
    rcv.show()
    

tcp.flags = 'PA'
mesaj = Raw()
mesaj.load = "123"
pachet = ip/tcp/mesaj
send(pachet)
tcp.seq += 3

tcp.flags = 'FA'
FIN = ip / tcp
raspuns_fin_ack = sr1(FIN)
raspuns_fin_ack.show()
tcp.seq += 1
tcp.ack = raspuns_fin_ack.seq + 1
tcp.flags = 'A'
ACK = ip / tcp
send(ACK)
