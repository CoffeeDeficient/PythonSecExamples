#!/usr/bin/python

import signal

def sigint_handler(signum, frm):
    print("It's not my time to die")

signal.signal(signal.SIGINT, sigint_handler)

while True:
    pass