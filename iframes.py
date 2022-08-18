from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("./chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
print("before frames- ", driver.find_element(By.TAG_NAME, "h3").text)
driver.switch_to.frame("mce_0_ifr")
#driver.switch_to.frame(driver.find_element(By.XPATH,"//*[contains(.,'Your content goes here.')]"))
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("this is laxman")
print(driver.find_element(By.CSS_SELECTOR, "#tinymce").text)#if the scope is inside the frame this will give the text

#if we want to check the other element outside the frames scope this will give the exception no such element exception
#driver.find_element(By.TAG_NAME, "h3").text
# to overcome the above problem user should switch back to the driver mode byt using default_contents method

print(driver.switch_to.parent_frame())
print(driver.find_element(By.TAG_NAME, "h3").text)

# driver.switch_to.default_content()
# print(driver.find_element(By.TAG_NAME, "h3").text)

#driver.find_element(By.ID,"tinymce").clear()#thiss will give you the exception
driver.get_screenshot_as_png()
#driver.close()
