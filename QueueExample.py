#!/usr/bin/python

import threading
import Queue
import time


class WorkerThread(threading.Thread):

    def __init__(self, q) :
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        print("In WorkerThread")
        while True:
            counter = self.q.get()
            print("Sleeping for %d"%counter)
            time.sleep(counter)
            print("Resuming from sleep")
            self.q.task_done()

q = Queue.Queue()

for i in range(10):
    print("Creating worker thread: %d"%i)
    worker = WorkerThread(q)
    worker.setDaemon(True)
    worker.start()
    print("Worker thread %d created!"%i)

for j in range(10):
    q.put(j)

q.join()
print("All tasks complete")