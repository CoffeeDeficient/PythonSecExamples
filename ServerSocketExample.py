#!/usr/bin/python

import socket
import threading
import Queue

#Build socket and listen
lport=8080
tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Ensure socket reuse
tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsocket.bind(("0.0.0.0", lport))
tcpsocket.listen(2)
print("Listening on %d..."%lport)

#Client handler thread to echo back input
class ClientThread(threading.Thread):
    
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        while True:
            rcvdata = '0'
            clientconn = self.q.get()
            client, conn = clientconn
            ip, port = conn
            while len(rcvdata):
                rcvdata = client.recv(2048)
                print("Received from Client: %s"%str(rcvdata))
                client.send(rcvdata)

            print("Closing connection to %s:%d..."%(ip,port))
            client.close()


if __name__ == "__main__":
    #Receive connections
    #Create a queue to manage incoming connections
    q = Queue.Queue()

    #Create 3 handlers
    for i in range(3):
        print("Creating client thread: %d"%i)
        clienthandler = ClientThread(q)
        clienthandler.setDaemon(True)
        clienthandler.start()

    #Accept incoming connections and place them on the queue
    while True:
        (client, (ip, port)) = tcpsocket.accept()
        print("Connection from: %s:%d"%(ip,port))
        q.put((client, (ip, port)))
    