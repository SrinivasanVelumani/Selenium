from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

location = os.getcwd() #current directory location

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    src_obj = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
    
    '''download files in desires location'''
    #plugins.always_open_pdf_externally:True(when we download pdf it opens , not download so to avoid that we use)
    
    preferences = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    #preferences = {"download.default_directory":"C:/Users/hp/Desktop/Selenium"}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    
    driver = webdriver.Chrome(service=src_obj,options=ops)
    driver.implicitly_wait(20)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    src_obj = Service("download edge driver.exe")
    
    '''download files in desires location'''
    #plugins.always_open_pdf_externally:True(when we download pdf it opens , not download so to avoid that we use)

    preferences = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    #preferences = {"download.default_directory":"C:/Users/hp/Desktop/Selenium"}
    
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preferences)
    
    driver = webdriver.Edge(service=src_obj,options=ops)
    driver.implicitly_wait(20)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    src_obj = Service("download firefox driver.exe")
    
    ops = webdriver.FirefoxOptions()
    #application/msword -- mime type(what type of application)
    #https://www.sitepoint.com/mime-types-complete-list/ #link to find extension type
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting",False)
    
    #to download in desired location
    # 0- desktop download, 1 in downloads  download, 2 specific location
    ops.set_preference("browser.download.folderList", 2)
    #if 2 means next line is required
    ops.set_preference("browser.download.dir",location)
    
    ops.set_preference("pdfjs.disabled", True)#to download pdf note mime also need to be changed
    
    driver.Edge(service=src_obj,options=ops)
    driver.implicitly_wait(20)
    return driver


driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")

driver.switch_to.frame("aswift_4")
driver.find_element(By.XPATH, "//*[normalize-space()='Download sample DOC file']/a[1]").click()
