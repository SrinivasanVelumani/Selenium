"""https://www.youtube.com/watch?v=gylMKXr40v0&list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&index=5&ab_channel=SDET-QAAutomation"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=src_obj)

'''1) app commands'''

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

#i) title of page 
print(driver.title)

#ii) current url 
print(driver.current_url)

#iii) page source code  
print(driver.page_source) # full html source code with css and all


'''2) conditional commands'''

driver.get("https://demo.nopcommerce.com/register")

#i) is_displayed() and is_enabled() can be used for any kind of elements

search_box = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print(search_box.is_displayed())
print(search_box.is_enabled())

#ii) is_selected() for radio buttons and check buttons   

rd_male = driver.find_element(By.CSS_SELECTOR,"label[for='gender-male']")
rd_female = driver.find_element(By.CSS_SELECTOR,"label[for='gender-female']")
print("..before selecting..")
print(rd_male.is_selected())    #false
print(rd_female.is_selected())  #false
rd_male.click()
print("...after male button is clicked..")
print(rd_male.is_selected())     #true
print(rd_female.is_selected())   #false
rd_female.click()
print("..after female button is clicked..")
print(rd_male.is_selected())     #false
print(rd_female.is_selected())   #true


'''3) Browser Commands'''

#i) driver quit() driver close()
driver.quit()
driver.close() #closes the first opened tab (driver.get(1st url))


''' 4) navigational commands forward,backward,refresh '''

driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.in/")

#i) back()
driver.back() #go to snap

#ii) forward()
driver.forward() #got to amazon

#iii) refresh()
driver.refresh()

''' 5) Wait Commands '''

#i) implicity_wait(10)     
      #works based on the time
      #wait for 10 seconds, still no element found raise exception 
        # we need to create after immediately after driver, so it apply for all , 
      #so we no need to apply separately
    
src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=src_obj) 
driver.implicitly_wait(10) 

#ii) explicity_wait()
     # works based on the condition
    # wait for 10 seconds, still no element will go for next step execution
    # need to create it for each web elements

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException


src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=src_obj) 

#mywait = WebDriverWait(driver, 10) #explicit object declaration , it will rise exception if no element within 10sec
#note: poll_frequnecy (if wait is 10sec and pf=2, it will split into 5 2secs and check elements for 5 times for each 2seconds)
mywait = WebDriverWait(driver, 10, poll_frequency=2,ignored_exceptions=[TimeoutException,  
                                                      Exception,
                                                      NoSuchElementException,
                                                      ElementNotVisibleException,
                                                      ElementNotSelectableException])

driver.get("https://www.google.com/")

search_box = driver.find_element(By.XPATH,"//input[@title='Search']")
search_box.send_keys("selenium")
search_box.submit()

search_link = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='selenium']"))) #this case will be failed
search_link.click()

search_link = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
search_link.click()