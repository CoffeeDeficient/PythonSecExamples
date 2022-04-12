#!/usr/bin/python
#Simple TCP listener with SIGALARM based timer
#TODO: Error handling


import socket
import os
import signal
import argparse

def tcpserver(port):
    #Build TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('localhost',port)
    s.bind(addr)

    #Listen
    s.listen(1)
    print("Listening on %d...\n"%port)

    #Handle connections and print received input
    while True:
        connection,client = s.accept()
        try:
            print("Connection: %s"%str(client))
            while True:
                #Do something interesting..
                rcv = connection.recv(32)
                print(rcv)
        finally:
            connection.close()

#Use SIGALARM to terminate after interval
def sigalarm_handler(signum, frm):
    print("Time is up!")
    quit()

if __name__ == "__main__":

    #Parse command line arguments
    parser = argparse.ArgumentParser(description="Timed TCP listener")
    parser.add_argument('-s', '--seconds', dest='secs', required=True, type=int, default=10, help="Seconds to listen")
    parser.add_argument('-p', '--port', dest='lport', required=True, type=int, default=8080, help="Listening port")
    args = parser.parse_args()

    #Install signal handler
    signal.signal(signal.SIGALRM, sigalarm_handler)
    #Alarm after specified time
    signal.alarm(args.secs)

    #Start tcp listener
    tcpserver(args.lport)