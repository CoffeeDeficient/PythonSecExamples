#!/usr/bin/python

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


html = urlopen("http://www.securitytube.net/video/3000")
print(html.code)

bt = BeautifulSoup(html.read(), "lxml")
print(bt.title.string)

#Get single next tag
print(bt.meta)
print(bt.meta.next)

#Get all meta tags
print("Get All Meta Tag:\n")
allMetaTags = bt.find_all('meta')
print(allMetaTags)
print(allMetaTags[0])
print(allMetaTags[1])

print(allMetaTags[0]['content'])

#Get ALl Links
print("Get All Links:\n")
allLinks = bt.find_all('a')
for link in allLinks:
    print(link['href'])

#Get All Text
print("Get All Text:\n")
allText = bt.get_text()
print(allText)

#Get Description
print("Get Description Links and Text:\n")
matches = re.compile("Description:|Tags:")
paras = bt.find_all('p')
for para in paras:
    matchobj  = matches.search(str(para))
    if(matchobj):
        print(para.get_text())
    
#Get Video
print("Get Video Link:\n")
video = bt.find('iframe', {'title' : 'YouTube video player'})
videoLink = video['src']
print(video)
print(videoLink)
