#!/usr/bin/python

import SocketServer

class ClientHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        ip,port = self.client_address
        print("Connection from %s..."%str(ip))
        rcvdata='0'

        while len(rcvdata):
            rcvdata = self.request.recv(1024)
            print("Client: %s"%str(rcvdata))
            #Echo back
            self.request.send(rcvdata)
        print("Client disconnect...")

srvAddr = ('0.0.0.0', 8080)
server = SocketServer.TCPServer(srvAddr, ClientHandler)
server.serve_forever()