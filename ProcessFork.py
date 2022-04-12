#!/usr/bin/python

import os

def child_process():
    print("child process - PID:  %d" % os.getpid())
    print("child exiting")

def parent_process():
    print("parent process - PID: %d"%os.getpid())
    
    childid = os.fork()
    if childid == 0 :
        child_process()
    else:
        print("Inside parent process")
        print("   Child PID: %d"%childid)

    while True:
        pass

parent_process()