#!/usr/bin/python

import thread
import time

def worker_thread(id):
    count = 1
    print("Thread %d started"%id)
    while True:
        print("Thread ID: %d  Counter: %d"%(id,count))
        time.sleep(3)
        count += 1

for i in range(5):
    thread.start_new_thread(worker_thread, (i,))

print("Main thread - infinte while")

while True:
    pass