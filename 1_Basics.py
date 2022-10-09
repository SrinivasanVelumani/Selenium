from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_ob = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_ob)


driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
driver.find_element(By.NAME,'Email').clear()
driver.find_element(By.NAME,'Email').send_keys("admin@yourstor.com")
driver.find_element(By.CLASS_NAME,'password').clear()
driver.find_element(By.CLASS_NAME,'password').send_keys("admin")
driver.find_element(By.CLASS_NAME,'buttons').click()
title = driver.title
if title=="Dashboard / nopCommerce administration":
    print("login success")
else:
    print("login failed")
driver.close()

