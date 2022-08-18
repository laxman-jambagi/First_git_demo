from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("./chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])
child_window_text = driver.find_element(By.TAG_NAME, "h3").text
assert "New Window" in child_window_text
driver.close()
driver.switch_to.window(windows_opened[0])
parent_window_text = driver.find_element(By.TAG_NAME, "h3").text
print("modified code in child window_1")

assert "Opening a new window" in parent_window_text

driver.close()
