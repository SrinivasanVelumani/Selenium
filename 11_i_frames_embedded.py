from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=src_obj)


'''1) independent frames within page'''

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

#SWITCH TO FRAME(NAME or ID or webelement (see eg inner frames) or 0 if one frame)

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()

'''2) inner frames (frames within frames)'''

driver.get("https://demo.automationtesting.in/Frames.html")

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outer_frame = driver.find_element(By.XPATH,"//iframe[src='MultipleFrames.html']") #outer frame 
driver.switch_to.frame(outer_frame)

inner_frame = driver.find_element(By.XPATH,"//iframe[src='MultipleFrames.html']") #inner frame 
driver.switch_to.frame(inner_frame)

#after switching to inner frame find webelement and perform actions
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()

#if needed
driver.switch_to.parent_frame() #go to outer frame