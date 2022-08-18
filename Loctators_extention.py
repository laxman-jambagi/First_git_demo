from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("./Chromedriver/chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.maximize_window()
# invoke the browser with URL by using get method
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
#form div:nth-of-type(3) or form div:nth-child(3)
drop=Select(driver.find_element(By.LINK_TEXT, "Forgot password?"))

