
'''https://www.youtube.com/watch?v=P0VTHIUeh2M&list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&index=7&ab_channel=SDET-QAAutomation'''
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=src_obj)

'''internal and external links'''

driver.get("https://demo.nopcommerce.com/")

total = driver.find_element(By.LINK_TEXT,"Digital downloads").click() # single link
total = driver.find_elements(By.TAG_NAME,"a") # all links using tag name
total = driver.find_elements(By.XPATH,'//a') # all links using xpath

'''broken links validate'''

driver.get("http://www.deadlinkcity.com/")

links = driver.find_elements(By.TAG_NAME,'a')
print(len(links))
count = 0

for link in links:
    url = link.get_attribute("href")
    res = requests.head(url)
    if res.status_code>=400:
        print("broken link")
        count+=1
        
print(count)