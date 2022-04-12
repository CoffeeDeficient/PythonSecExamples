#!/usr/bin/python

import threading
import time

file = open("test.txt","a")


class filewriter(threading.Thread):
   
    def __init__(self, file, myid, threadlock):
        threading.Thread.__init__(self)
        self.file = file
        self.myid = str(myid)
        self.threadlock = threadlock
    
    def run(self):
        count = 0        
        while count<10:
            print("Waiting on lock (%s)"%self.myid)
            with self.threadlock:
                print("Obtained lock")
                self.file.write(self.myid)
                print("%s count: %d"%(self.myid,count))
                count+=1
                time.sleep(1)

threadlock = threading.Lock()
for i in range(5):
    print("Creating thread: %d"%i)
    worker = filewriter(file,i,threadlock)
    worker.setDaemon(True)
    worker.start()
    print("Worker thread %d created!"%i)

time.sleep(90)

