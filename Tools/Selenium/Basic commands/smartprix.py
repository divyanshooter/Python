from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from seleniumbase import Driver
import time

# options=  webdriver.ChromeOptions()
# options.add_experimental_option('detach',True)

#driver=webdriver.Chrome(options=options,service=s)
driver = Driver(uc=True)

driver.get("https://www.smartprix.com/mobiles")
time.sleep(2)

driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(2)

driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(2)

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

with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)

time.sleep(10)