#!/usr/bin/python

import socket
import struct
import binascii


rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
ip_proto = 0
while ip_proto != 6:
    pkt = rawSocket.recvfrom(2048)
    ethernetHeader = pkt[0][0:14]
    eth_hdr = struct.unpack("!6s6s2s", ethernetHeader)

    eth_dstmac = binascii.hexlify(eth_hdr[0])
    eth_srcmac = binascii.hexlify(eth_hdr[1])
    eth_type = binascii.hexlify(eth_hdr[2])

    ipHeader = pkt[0][14:34]
    ip_hdr = struct.unpack("!8sBB2s4s4s", ipHeader)
    ip_proto = ip_hdr[2]

print("Ethernet")
print(" SRC MAC: " + eth_srcmac)
print(" DST MAC: " + eth_dstmac)
print(" Type: " + eth_type)
print("IP")
print(" Protocol: " + str(ip_hdr[2]))
print(" Source IP: " + socket.inet_ntoa(ip_hdr[4]))
print(" Destination IP: " + socket.inet_ntoa(ip_hdr[5]))

tcpHeader = pkt[0][34:54]
tcp_hdr = struct.unpack("!HHLL8s", tcpHeader)

print("TCP")
print(" Source Port: " + str(tcp_hdr[0]))
print(" Destination Port: " + str(tcp_hdr[1]))
print(" Sequence Number: " + str(tcp_hdr[2]))
print(" Ack Number: " + str(tcp_hdr[3]))
print(" Flags Etc: " + str(binascii.hexlify(tcp_hdr[4])))