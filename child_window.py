from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("./chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"openwindow").click()
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])
driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium Webdriver with Java Basics").click()

#print(driver.title)

