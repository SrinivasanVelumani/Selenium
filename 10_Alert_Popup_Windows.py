from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=src_obj)


'''1) normal alerts and popups'''

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
alert_pop = driver.switch_to.alert
print(alert_pop.text) #alert popup text
alert_pop.send_keys("hi") #if there is some input box in alert popup
alert_pop.accept() # ok button click 
alert_pop.dismiss() #cancel buton click

'''2) Authentication popups'''

#syntax https://username:password@url (url injection)

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")


'''3) notifications ''' # we cannot handle this type using switch_to.alert, so e disable it

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
disable_not = webdriver.ChromeOptions()
disable_not.add_argument('--disable-notifications')
driver = webdriver.Chrome(service=src_obj,options=disable_not)
