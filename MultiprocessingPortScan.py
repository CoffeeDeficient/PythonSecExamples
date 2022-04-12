#!/usr/bin/python

from multiprocessing.process import current_process
from sys import flags
from scapy.all import *
import logging
from multiprocessing import Pool


#logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

dst_ip=sys.argv[1]
src_prt = RandShort()
lowport = int(sys.argv[2])
highport = int(sys.argv[3])
ports = [i for i in range(lowport,highport)]


print("Scanning: %s from %d to %d\n"%(dst_ip,lowport,highport))

def portscan(port):
    print("SCANNING: %d (PID: %d)"%(port,current_process().pid))
    ip=IP(dst=dst_ip)
    syn=TCP(sport=src_prt,dport=port,flags='S',seq=1000)
    resp=sr1(ip/syn,verbose=False)

    if str(type(resp)) == "<type 'NoneType'>":
        return -1
    elif resp.haslayer(TCP):
        if resp.getlayer(TCP).flags == 0x12:
            send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_prt, dport=port, flags='AR'), timeout=1)
            return port
        elif resp.getlayer(TCP).flags == 0x14:  
            return -1


if __name__ == "__main__":
    pool = Pool(4)
    result = pool.map(portscan, range(lowport, highport),20)
    for i in result:
        if int(i)>-1:
            print("%d Open"%i)


    
    
    
    
    
    
