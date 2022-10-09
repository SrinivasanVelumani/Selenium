from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datetime import date as today_date

src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=src_obj)
driver.implicitly_wait(100) 

driver.get("https://testautomationpractice.blogspot.com/?")
date_ui = driver.find_element(By.XPATH,"//input[@id='datepicker']")
#date_ui.send_keys("05/03/2001")
date_ui.click()

choose_day = "Tu"
choose_date = '15'
choosed_month = 'December'
choosed_year = '2022'

month_dict={"January":1,"February":2,"March":4,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,
            "October":10,"November":11,"December":12}

prev_cl = 0
next_cl = 0


while True:
    prev_button = driver.find_element(By.XPATH,"//a[@title='Prev']")
    next_button = driver.find_element(By.XPATH,"//a[@title='Next']")
    
    month = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    year =  driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    
    if choosed_year == year:
        if choosed_month == month:
            # days = driver.find_elements(By.XPATH,"//th[@scope='col']")
            # for day in days:
            #     if day.text == choose_day:
            #         day.click()
            #         break  
                
            dates = driver.find_elements(By.XPATH,"//td[@data-year="+year+"]")
            for date in dates:
                if date.text == choose_date:
                        date.click()
                        break
            break
        
        elif choosed_month != month:
            if month_dict.get(choosed_month) < month_dict.get(month):
                prev_button.click()
            
        elif choosed_month != month:
            if month_dict.get(choosed_month) > month_dict.get(month):
                next_button.click()

    elif choosed_year < year:
        prev_button.click()
        
    elif choosed_year > year:
        next_button.click()

        
print(date_ui.get_attribute('value'))
driver.quit()
