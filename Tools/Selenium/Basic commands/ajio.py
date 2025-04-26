from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from seleniumbase import Driver
import time

s=Service("/Users/divyanshuchaturvedi/Documents/Documents/Learning/chromedriver-mac-arm64/chromedriver")

options=  webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

#driver=webdriver.Chrome(options=options,service=s)
driver = Driver(uc=True)

driver.get("https://www.ajio.com/men-backpacks/c/830201001?srsltid=AfmBOorjLowY2LZfsafp0Le84u__pgOE2_4qEQHVVLOTQXshjEFOIrco")

old_height = driver.execute_script('return document.body.scrollHeight')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    new_height=driver.execute_script('return document.body.scrollHeight')
    if new_height==old_height:
        break
    old_height=new_height

html=driver.page_source
#print(html)

# with open('ajio.html','w',encoding='utf-8') as f:
#     f.write(html)