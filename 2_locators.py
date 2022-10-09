from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_ob = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_ob)

'''1) locators'''

driver.get("http://automationpractice.com/index.php")

#i) name
driver.find_element(By.NAME,'Email').send_keys("admin@yourstor.com")

#ii)id
driver.find_element(By.ID,'Email').send_keys("admin@yourstor.com")

# iii) LINK_TEXT
driver.find_element(By.LINK_TEXT,'eg: click here').click()

# iv) PARTIAL_LINK_TEXT
driver.find_element(By.PARTIAL_LINK_TEXT,'eg: click').click()

# v) CLASS_NAME
sliders = driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(sliders)
print(len(sliders))

# vi) TAG_NAME
links = driver.find_elements(By.TAG_NAME,"a")
print(links)
print(len(links))


'''2) CSS Selectors'''

driver.get("https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjY0OTc0OTMyLCJjYWxsc2l0ZV9pZCI6MjY5NTQ4NDUzMDcyMDk1MX0%3D")

#i) tag and id
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("hi")
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("hi")

#ii) tag and class
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("hi")
driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("hi")

#iii) tag attribute
driver.find_element(By.CSS_SELECTOR,"input[name=email]").send_keys("hi")
driver.find_element(By.CSS_SELECTOR,"[name=email]").send_keys("hi")

#iv) tag class attribute (facebook test)
driver.find_element(By.CSS_SELECTOR,"input.inputtext[name=email]").send_keys("hi")


'''3) xpath'''

driver.get("http://automationpractice.com/index.php")

#i) absolute x path
driver.find_element(By.XPATH,'/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]').send_keys("T Shirts")
driver.find_element(By.XPATH,'/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button').click()

#ii) relative xpath
driver.find_element(By.XPATH,'//input[@id="search_query_top"]').send_keys("T Shirts")
driver.find_element(By.XPATH,'//*[@id="searchbox"]/button').click()
driver.find_elements(By.XPATH, "//div[@class='footer']//a") #selects all a tags in under class footer

#iii) relative xpath or,and, contains(), starts-with(), text()
driver.get("https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjY0OTc0OTMyLCJjYWxsc2l0ZV9pZCI6MjY5NTQ4NDUzMDcyMDk1MX0%3D")
driver.find_element(By.XPATH,'//*[@id="email" or @placeholder="Email address or phone number"]').send_keys("T Shirts")
driver.find_element(By.XPATH,'//*[@id="email" and @placeholder="Email address or phone number"]').send_keys("T Shirts")
driver.find_element(By.XPATH,'//input[contains(@id,"email")]').send_keys("hi")
driver.find_element(By.XPATH,'//input[starts-with(@id,"email")]').send_keys("hi")
driver.find_element(By.XPATH,'//a[text()="Forgotten account?"]').click()
