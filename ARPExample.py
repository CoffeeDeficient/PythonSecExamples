#!/usr/bin/python

from itertools import chain
import socket
import struct

def macformat(mac):
    mac = mac.split(":")
    maclist = list()
    for i in mac:
        maclist.append(int(i,16))
    return tuple(maclist)

def ipformat(ip):
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L",packedIP)[0]

if __name__ == "__main__":
    #Build ARP packet (0x0806)
    rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
    rawSocket.bind(("eth0", 8))

    #Eth
    ether_ip_src_mac = "aa:bb:cc:dd:ee:ff"
    ether_ip_dst_mac = "FF:FF:FF:FF:FF:FF"
    ether_type = 0x0806
    #ARP
    arp_htype = 0x0001
    arp_ptype = 0x0800
    arp_hlen = 0x06
    arp_plen = 0x04
    arp_op = 0x0001
    arp_src_ip = "0.0.0.0"
    arp_dst_mac = "00:00:00:00:00:00"
    arp_dst_ip = "192.168.1.14"

    ip_s_mac = macformat(ether_ip_src_mac)
    ip_d_mac = macformat(ether_ip_dst_mac)
    s_ip = ipformat(arp_src_ip)
    arp_d_mac = macformat(arp_dst_mac)
    d_ip = ipformat(arp_dst_ip)

    ether_header = struct.pack("!6B6BH", *tuple(chain(ip_d_mac, ip_s_mac, [ether_type])))
    arp_data = struct.pack("!HHBBH6BI6BI",
        *tuple(chain(
            [arp_htype, arp_ptype, arp_hlen, arp_plen, arp_op], ip_s_mac,
            [s_ip], arp_d_mac, [d_ip]
        ))
    )

    ## Min length for ethernet frame sans 802.1Q tag is 46 bytes
    while len(arp_data) < 46:
        arp_data += struct.pack("B", 0x00)

    packet = ether_header + arp_data
    rawSocket.send(packet)
    rawSocket.close()

