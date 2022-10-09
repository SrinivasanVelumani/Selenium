from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=src_obj)

driver.get("https://demo.nopcommerce.com/")


'''1) find _element'''

# i) locator pointing single web element
home = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
home.send_keys("Apple MacBook Pro 13-inch")

# ii) locator pointing multi web element
home = driver.find_element(By.XPATH, "//div[@class='footer']//a")
print(home.text)

#iii) if no web elements found it rise exception in find_element


'''2) find_elements'''

# i) locator pointing single web element
home = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
print(home[0].txt) #[0] is bcz it is list even it is sing element returning
print(len(home))
home[0].send_keys("Apple MacBook Pro 13-inch")

# ii) locator pointing multi web elements
home = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(home))
print(home[0].text)
for ele in home:
    print(ele.text)

#iii) if no web elements found it does not show any exception in find_elements