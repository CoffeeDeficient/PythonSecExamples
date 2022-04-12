from scapy.all import *

def httpextract(packet):
    
    if (packet.haslayer("Raw")):
        #Look for HTTP assuming filter
        rawlayer = str(packet.getlayer('Raw')).split("\r\n")
        if(packet.haslayer(IP)):
            #Get IP src/dst
            srcip = packet.getlayer(IP).src
            dstip = packet.getlayer(IP).dst
        
        print("Src: " + srcip)
        print("Dst: " + dstip)
        print("\n")
        for i in rawlayer:
            print(i)
        print("------------------------------------------------\n")
    else:
        pass


if __name__=="__main__":
    sniff(iface="eth0",filter="tcp port 80",prn=httpextract)