from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

src_ob = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=src_ob)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()


'''1) scroll down based on pixels'''

driver.execute_script("window.scrollBy(0,3000)","")
value = driver.execute_script("return window.pageYOffset;")
print(value)


'''2) scroll down till element is visible'''

india_ele = driver.find_element(By.XPATH,"//td[normalize-space()='India']")
driver.execute_script("arguments[0].scrollIntoView();",india_ele)
value = driver.execute_script("return window.pageYOffset;")
print(value)


'''3) scroll down till end of the page'''

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") #navigate to end
value = driver.execute_script("return window.pageYOffset;")
print(value)

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)") #navigate to start again
value = driver.execute_script("return window.pageYOffset;")
print(value)