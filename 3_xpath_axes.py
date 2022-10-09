'''important'''
#https://www.youtube.com/watch?v=XL2pU5y3Kf8&list=PLUDwpEzHYYLsuUBvuoYTlN0KsBB5t-BDa&ab_channel=SDET-QAAutomation
#(* can be relaced by tag names)
'''.............................'''


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_ob = Service("C:/Users/hp/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser_ob)

driver.get("https://money.rediff.com/gainers")

#i) self "//a[contains(text(),'India Tourism De')]" - self node
txt_msg = driver.find_element(By.XPATH, "//a[contains(text(),'India Tourism De')]/self::a").text
print(txt_msg)


#ii) parent
txt_msg = driver.find_element(By.XPATH, "//a[contains(text(),'India Tourism De')]/parent::td").text
print(txt_msg)


#iii) child 
        #note: 1) in that link a tag (self node) does not have child so we jump to parent and find childs for parent 
        #          2) in that link a tag (self node) does not have child so we jump to ancestor and find childs for ancestors    

child = driver.find_elements(By.XPATH, "//a[contains(text(),'India Tourism De')]/parent::td/child::a")
for i in child:
    print(i.text)

child = driver.find_elements(By.XPATH, "//a[contains(text(),'India Tourism De')]/ancestor::tr/child::td")
for i in child:
    print(i.text)
    
    
#iv) ancestor 
     #note (main tags selects)
ancestor = driver.find_elements(By.XPATH, "//a[contains(text(),'India Tourism De')]/ancestor::tr")
print(ancestor)


#v) descendent 
    #note (select all tags under particular ancestor or parent) 1) (all tags selected if * is used descendant::*)  
    #     2) in that link a tag (self node) does not have decendent so we jump to ancestor and find descendent for ancestor
descendent = driver.find_elements(By.XPATH, "//a[contains(text(),'India Tourism De')]/ancestor::tr/descendant::*")
for i in descendent:
    print(i.text)

descendent = driver.find_elements(By.XPATH, "//a[contains(text(),'India Tourism De')]/ancestor::tr/descendant::td")
for i in descendent:
    print(i.text)


#vi) Following  (eg: row with coloumns (like box box))
    #selects all tags (entire tags in page) below the slef node ancestor or parent
followings = driver.find_elements(By.XPATH, "//a[contains(text(),'India Tourism De')]/ancestor::tr/following::*")
print(len(followings))


#vii) following sibling (parallel) (eg: all row in same single line))
followings = driver.find_elements(By.XPATH, "//a[contains(text(),'India Tourism De')]/ancestor::tr/following-sibling::*")
print(len(followings))


#viii) preceding 
preceding = driver.find_elements(By.XPATH, "//a[contains(text(),'India Tourism De')]/ancestor::tr/preceding::*")
print(len(preceding))


#viii) preceding sibling
preceding = driver.find_elements(By.XPATH, "//a[contains(text(),'India Tourism De')]/ancestor::tr/preceding-sibling::*")
print(len(preceding))