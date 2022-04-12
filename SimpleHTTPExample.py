#!/usr/bin/python

import SocketServer
import SimpleHTTPServer

class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        if self.path == '/admin':
            print("Request for admin")
            self.wfile.write('Access Denied!\n')
            #Return the client headers
            self.wfile.write(self.headers)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


httpsrvr = SocketServer.TCPServer(('127.0.0.1', 8080), HttpRequestHandler)
httpsrvr.serve_forever()