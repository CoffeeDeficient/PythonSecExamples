#!/usr/bin/python

from sys import flags
from scapy.all import *
import logging
from threading import Thread


#logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

dst_ip=sys.argv[1]
src_prt = RandShort()
lowport = int(sys.argv[2])
highport = int(sys.argv[3])
ports = [i for i in range(lowport,highport)]


print("Scanning: %s from %d to %d"%(dst_ip,lowport,highport))

def portscan(portrange):
    print("INside thread: ")
    print(portrange)
    print("SCANNING: " + str(portrange[0]) +":"+ str(portrange[-1]))
    for port in portrange:
        ip=IP(dst=dst_ip)
        syn=TCP(sport=src_prt,dport=port,flags='S',seq=1000)
        resp=sr1(ip/syn)


        #p = IP(dst=dst_ip)/TCP(sport=src_prt, dport=port, flags='S') # Forging SYN packet
        #resp = send(syn,verbose=False)
        #resp = sr1(p, timeout=2) # Sending packet
        if str(type(resp)) == "<type 'NoneType'>":
            print("Closed Port: %d"%port)
        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12:
                send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_prt, dport=port, flags='AR'), timeout=1)
                print("Open port: %d"%port)
                #openp.append(port)
            elif resp.getlayer(TCP).flags == 0x14:  
                print("Closed Port: %d"%port)

subset = list()
print(ports)
for i in range(0, len(ports), 20):
    subset.append(ports[i:i+20])
print(subset)
for x in subset:
    t = Thread(target=portscan,args=(x,))
    t.start()
    
    
    
    
    
    
