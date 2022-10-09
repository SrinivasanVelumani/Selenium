from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=src_obj)


'''1) static Table'''

driver.get("https://testautomationpractice.blogspot.com/?")

# 1) count number of or rows and columns

total_rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
total_col = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th"))
print(total_rows)
print(total_col)

# 2) particular row and column data (using proper xpath)

data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td[2]")
print(data.text)

# 3) using loop

for i in range(2,total_rows+1):
    for j in range(1,total_col+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/"+"tr"+str([i])+"/"+"td"+str([j])).text
        print(data,end=" ") 
    print(" ")

# 4) Conditional based data retreive (eg: author name (2nd colom) mugesh data retreive)

author_col = 2
book_name_col = 1
for i in range(2,total_rows+1):
    data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/"+"tr"+str([i])+"/"+"td"+str([author_col])).text
    if data == 'Amit':
        print(driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/"+"tr"+str([i])+"/"+"td"+str([book_name_col])).text)
driver.quit()

'''2) Dynamic Table'''    

'''same as we did for static table--- capture all rows and use len(), and mostly coloumn will be same'''
