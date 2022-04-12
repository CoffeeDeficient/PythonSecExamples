#!/usr/bin/python

import ftplib
import threading
import Queue

serverlist = [ "ftp.gnu.org", "ftp.pureftpd.org", "ftp.vim.org", "ftp.slackware.com"]

class ftpdiscoverythread(threading.Thread):
    
    def __init__(self, q) :
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        while True:
            server = self.q.get()
            print("Connecting to %s"%server)
            try:
                ftp = ftplib.FTP(server)
                ftp.connect()
                ftp.login()
                file_list = ftp.nlst()                
                print("\nFile List for %s:"%server)
                print(file_list)
                prtin("\n")
                ftp.close()
            except:
                print("Failed to connect to %s"%server)
            finally:
                self.q.task_done()

q = Queue.Queue()

for i in range(5):
    print("Creating worker thread: %d"%i)
    worker = ftpdiscoverythread(q)
    worker.setDaemon(True)
    worker.start()
    print("Worker thread %d created!"%i)

for i in serverlist:
    q.put(i)

q.join()
print("Server list complete")

