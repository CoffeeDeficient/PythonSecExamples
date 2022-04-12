#!/usr/bin/python

from scapy.all import *

def wifi_ssid_extract(packet):
    if packet.haslayer(Dot11):
        print("WiFi!")
        if ((packet.type == 0) and (packet.subtype == 8)):
            print(packet.addr2)
            print(packet.info)

if __name__=="__main__":
    sniff(iface="wlx00c0caae54cf", prn=wifi_ssid_extract)
