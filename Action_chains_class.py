from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj=Service("./chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.click_and_hold(driver.find_element(By.ID,"mousehover")).perform()
# action.context_click(driver.find_element(By.XPATH,"//a[@href='#top']")).perform()
# action.double_click()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Top")).perform()
driver.get_screenshot_as_file("lll.jpeg")

driver.close()