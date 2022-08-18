from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=".//chromedriver/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com")
driver.find_element(By.LINK_TEXT, "Frames").click()
driver.find_element(By.LINK_TEXT, "Nested Frames").click()
# switch to frame with name
driver.switch_to.frame("frame-left")
# identify the element and get text method
s = driver.find_element(By.XPATH, "//body").text
print ("Test inside frame: " + s)
# move out of frame to the parent page
driver.switch_to.default_content()
driver.get_sinks()
driver.quit()
