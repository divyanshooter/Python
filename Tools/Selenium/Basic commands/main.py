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

driver.get("http://www.google.com")

user_input=driver.find_element(by=By.XPATH,value='//*[@id="APjFqb"]')
user_input.send_keys('campusx')



user_input.send_keys(Keys.ENTER)

link=driver.find_element(by=By.XPATH,value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div/div/span/a')
link.click()

link=driver.find_element(by=By.XPATH,value='//*[@id="1698390585510d"]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[2]')
link.click()
time.sleep(100)

