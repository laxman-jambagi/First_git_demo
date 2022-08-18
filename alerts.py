import time

from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
name = "Laxman"
service_obj=Service("./chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

#selenium will not handle the java/javascript alert popup.
#webdriver will not support for alert popup we need to switch from webdriver mode to alert mode
#to switching driver mode to alter we have one class    .switch_to.alert, create a object of alert and perform the action on alert popup
#or retrive the text on the popup
alert = driver.switch_to.alert

alerttext= alert.text
assert name in alerttext
alert.accept() #click on positive button like ok, confirm use accept() method
#alert.dismiss() #click on negative. like cancel, close


# alert.accept()# this method is used to click on ok
# driver.find_element(By.XPATH, "//input[@value='Confirm']").click()
# driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Mr Jambagi")
# print(alert.text)
# alert.dismiss()



