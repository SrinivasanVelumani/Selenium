
'''https://www.youtube.com/watch?v=P0VTHIUeh2M&list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&index=7&ab_channel=SDET-QAAutomation'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=src_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")

week_box = driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
print(len(week_box))

#1 aproach click all
for i in range(len(week_box)):
    week_box[i].click()
time.sleep(5)


#2 aproach for particular checkbox select
selc=['monday','wednesday','friday']
for checkbox in week_box:
    #print(checkbox.text) # inner text is not available
    if(checkbox.get_attribute('id') in selc):
        checkbox.click()

for checkbox in week_box:
    print(checkbox.is_selected())
time.sleep(5)


#3 select last 2 box,  use range(start,end)----(len(weekbox)-how many from last 2, len(week_box))


#4 to unselect -- again use click()
for checkbox in week_box:
    if checkbox.is_selected():
        checkbox.click()
        
for checkbox in week_box:
    print(checkbox.is_selected())