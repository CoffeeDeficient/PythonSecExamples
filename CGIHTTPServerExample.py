#!/usr/bin/python

import SocketServer
import BaseHTTPServer
import CGIHTTPServer
#import cgitb

#cgitb.enable()

class CGIRequestHandler(CGIHTTPServer.CGIHTTPRequestHandler):

    def do_GET(self):
        print(self.path)
        if self.path == '/admin':
            print("Request for admin")
            self.wfile.write('Access Denied!\n')
            #Return the client headers
            self.wfile.write(self.headers)
        elif self.path == '/cgi/spoof.py':
            self.wfile.write('Woot!')
        else:
            CGIHTTPServer.CGIHTTPRequestHandler.do_GET(self)

server = BaseHTTPServer.HTTPServer
cgihandler = CGIRequestHandler
lport = 8080

srvrAddr = ('127.0.0.1', lport)
cgihandler.cgi_directories = ['/cgi']

cgisrvr = server(srvrAddr, cgihandler)
cgisrvr.serve_forever()