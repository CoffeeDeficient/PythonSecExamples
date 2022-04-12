#!/usr/bin/python

import os

def getdir():
    return ("---")

def recursedir(path,depth):
    #print("Called recursedir:" + path)

    for i in os.listdir(path):
        #print(i)
        if (os.path.isdir(os.path.join(path,i))):
            print(depth*"---" + i + "(d)")
            recursedir(os.path.join(path,i),depth+1)
        elif (os.path.isfile(os.path.join(path,i))):
            print(depth*"---" + i +"(f)")


recursedir("../.",0)
