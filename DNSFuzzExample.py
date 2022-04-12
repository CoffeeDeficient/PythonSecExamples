#!/usr/bin/python

#DNS and ARP poisoning example
#Inspired by Pentester Academy example

from sys import argv
from scapy.all import *
import argparse

def fuzzdns():
    dnspkt = IP(dst=args.dnsip, src="10.60.60.11")/UDP()/fuzz(DNS())
    print(dnspkt.summary())
    sr(dnspkt,timeout=1)   

if __name__ == "__main__":
    #Parse command line arguments
    parser = argparse.ArgumentParser(description="DNS Fuzzer")
    parser.add_argument('-d', '--dns', dest='dnsip', required=True, help="Target DNS")
    parser.add_argument('-c', '--count', dest='pktcount', type=int, required=False, default=10, help="Maximum Packets")
    args = parser.parse_args()

    #Listen for DNS and send responses
    i = 0
    print("Sending fuzzed DNS packets...")
    while i<int(args.pktcount) :
        print("%d / %d\n"%(i,args.pktcount))
        fuzzdns()
        i += 1
