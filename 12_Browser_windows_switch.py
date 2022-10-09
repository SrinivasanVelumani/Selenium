from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=src_obj)


# i) single window id

driver.get("https://demo.nopcommerce.com/")
demo_parent = driver.current_window_handle

# ii) multiple window id (comes as list))

driver.get("https://demo.nopcommerce.com/")
child_window = driver.find_element(By.LINK_TEXT,'Facebook')
child_window.click()
time.sleep(5)

windows_id = driver.window_handles

#switching to particular window
driver.switch_to.window(windows_id[0]) #switch to parent window
time.sleep(5)

#closing particular window
driver.switch_to.window(windows_id[1])  #switch to child and close
driver.close()  #it closes the window where it is pointed to currently

#aproach 2 closing using title
for tab_id in windows_id:
    driver.switch_to.window(tab_id)
    time.sleep(5)
    if driver.title =='NopCommerce - Home | Facebook':
        driver.close()
    
    