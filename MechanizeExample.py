#!/usr/bin/python

import mechanize


br = mechanize.Browser()
br.open("http://www.securitytube.net/video/3000")

for form in br.forms():
    print(form)

br.select_form(nr=0)
br.form['q'] = 'defcon'
print(br.submit())

for link in br.links():
    print(link.url + " : " + link.text)
