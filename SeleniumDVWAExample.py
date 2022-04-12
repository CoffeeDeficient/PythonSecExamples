#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://10.60.60.12/dvwa")
elem = driver.find_element_by_name("username")
elem.clear()
elem.send_keys("admin")
elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys("password")

elem.send_keys(Keys.RETURN)

print(driver.title)
assert "Welcome" in driver.title
assert "blarg" in driver.title

driver.close()
