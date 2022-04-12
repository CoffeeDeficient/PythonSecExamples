#!/usr/bin/python

import mechanize

#Create CookieJar and use with browser1
browser1 = mechanize.Browser()
sharedcookies = mechanize.CookieJar()
browser1.set_cookiejar(sharedcookies)

#Attempt to access DVWA root
print("Num Cookies: %d"%len(sharedcookies))
browser1.open("http://10.60.60.12/dvwa/")
print(browser1.title())
print("Num Cookies: %d"%len(sharedcookies))

#Login to DVWA
#Only one form available
browser1.select_form(nr=0)
browser1.form['username'] = 'admin'
browser1.form['password'] = 'password'
browser1.submit()
browser1.response().read()
print(browser1.title())
print("Num Cookies: %d"%len(sharedcookies))

#Create browser2 with shared cookies and access DVWA root
browser2 = mechanize.Browser()
browser2.set_cookiejar(sharedcookies)
browser2.open("http://10.60.60.12/dvwa/")
#print(browser2.response().read())
browser2.response().read()
print(browser2.title())
print("Num Cookies: %d"%len(sharedcookies))

#Iterate throught cookies
print("\n")
for cookie in sharedcookies:
    print(cookie)
    #If value "high" set to "low"
    if "high" in str(cookie):
        print("CHanging to low...")
        cookie.value = 'low'

#Iterate through cookies to show change
print("\n")
for cookie in sharedcookies:
    print(cookie)
    print(cookie.value)



