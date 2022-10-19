from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=src_obj)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")

text_box_1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
text_box_2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

text_box_1.send_keys("hellooo welcome to selenium")

act=ActionChains(driver)

#1) ctrl A
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(3)
# or 
#act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#2) ctrl c
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(3)


text_box_2.click() #or tab act.key_down(Keys.TAB).perform()
time.sleep(3)

#3) ctrl v
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(3)