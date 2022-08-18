import time

from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("./chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()#checking check box
        time.sleep(3)
        checkbox.click()#unchecking check for selected check box
        time.sleep(5)
        break

assert not checkbox.is_selected()

time.sleep(5)
driver.close()
