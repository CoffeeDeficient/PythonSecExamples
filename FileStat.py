#!/usr/bin/python

import os

#Print file, stats (inode,links,size,a/c/m times)
for file in os.listdir("."):
    print(file)
    print(os.stat(file))
    #Alt
    print(os.path.getsize(file))


