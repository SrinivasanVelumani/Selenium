from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver= webdriver.Chrome(service=src_obj)

driver.get("https://demo.nopcommerce.com/login?ReturnUrl=%2Fadmin")

email = driver.find_element(By.XPATH,"//input[@id='Email']")
password = driver.find_element(By.XPATH,"//input[@id='Password']")
button = driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")


#.text - (hard coded value or name of the element or inner text) it prints the name alone text eg: <p id="sri"> hi </p> 
#so, it prints "hi" if xpath is like this //p[@id='sri']

print("email text: ", email.text) 
print("passsword text: ", password.text)
print("button text: ", button.text)

email.clear()
email.send_keys("sri@gmail.com")
password.send_keys("admin")

email_data = email.get_attribute("value")   #can be ("any attribute - id,name,etc")
email_pass = password.get_attribute("value")
email_button = button.get_attribute("type")

print("email get_attribute: ", email_data) 
print("passsword get_attribute: ", email_pass)
print("button get_attribute: ", email_button)

driver.quit()