'''https://www.youtube.com/watch?v=P0VTHIUeh2M&list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&index=7&ab_channel=SDET-QAAutomation'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=src_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")

country = Select(driver.find_element(By.XPATH,"//select[@name='country_id']"))

#i) select by visible text (preferrable)
country.select_by_visible_text("India")
time.sleep(5)

#ii) select by value
country.select_by_value("13")
time.sleep(5)

#iii) select by index
country.select_by_index(14)
time.sleep(5)

# iv) capture all the dropdowns and print them
print(len(country.options))

# vi) select dropdown without using inbuilt object
# iterate through for loop and match string and use click and break

'''important without select tag'''
#vii) if select tag is not there u cannot use above Select module
country_all = driver.find_elements(By.XPATH,"//*[@name='country_id']/option")
print(len(country_all)) 
   
driver.quit()