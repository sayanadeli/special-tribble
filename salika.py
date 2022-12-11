from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get('https://185.215.180.7/mine?wallet=007245E9C88435A60A79D7CF44CC07C6C1810F86F5618826EC')
sleep(86400)
