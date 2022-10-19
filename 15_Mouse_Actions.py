from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=src_obj)
driver.implicitly_wait(100) 


'''1) mouse hover'''

driver.get("http://automationpractice.com/index.php")
act= ActionChains(driver)

dress_element = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@class='header-container']/header[@id='header']/div/div[@class='container']/div[@class='row']/div[@id='block_top_menu']/ul[@class='sf-menu clearfix menu-content']/li[@class='sfHoverForce']/a[1]")
evening_dress = driver.find_element(By.XPATH,"//li[@class='sfHover']//a[@title='Evening Dresses'][normalize-space()='Evening Dresses']")

act.move_to_element(dress_element).move_to_element(evening_dress).click().perform()


'''2) right click'''

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

act = ActionChains(driver)

rht_button = driver.find_element(By.XPATH,"//span[normalize-space()='right click me']")

act.context_click(rht_button).perform()


'''3) double click'''

act.double_click(rht_button).perform()


'''4) drag and drop'''

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source_ele = driver.find_element(By.ID,"box3")
target_ele =  driver.find_element(By.ID,"box103")

act = ActionChains(driver)

act.drag_and_drop(source_ele, target_ele).perform()


'''5) slider'''

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

min_slide_point = driver.find_element(By.XPATH,"//span[1]")
max_slide_point = driver.find_element(By.XPATH,"//span[2]")

print("Before Moving")
print("x axis:", min_slide_point.location)
print("y axis:", max_slide_point.location)

act = ActionChains(driver)

#we are moving in x axis alone so in y 0
act.drag_and_drop_by_offset(min_slide_point, 100, 0).perform()
act.drag_and_drop_by_offset(max_slide_point, -39, 0).perform()

print("after Moving")
print("x axis:", min_slide_point.location)
print("y axis:", max_slide_point.location)

