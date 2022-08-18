import time

from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("./chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#test case seclect the radio2 button
radiobuttons = driver.find_elements(By.CLASS_NAME, "radioButton")#by using class name //3 elements found
# radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton") #by CSS_SELECTOR
# radiobuttons = driver.find_elements(By.XPATH, "//*[@class='radioButton']")# By XPATH
print(len(radiobuttons))
#if you know the element should be checked then direct click on the element
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

#if radio button dynamically changing go for iteration method
# for radiobutton in radiobuttons:
#     if radiobutton.get_attribute("value") == "radio3":
#         radiobutton.click()
#         assert radiobutton.is_enabled()# if radio button selected then test case is pass other wise test will fail.
#         break
# # assert radiobutton.is_selected()
# #time.sleep(30)


#check the hide and show text
assert driver.find_element(By.ID,"displayed-text").is_displayed()#
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()# false means true

driver.close()
