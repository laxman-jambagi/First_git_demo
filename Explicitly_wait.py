#ElementNotVisibleException
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#from selenium.webdriver.support.wait import WebDriverWait
service_obj = Service("./chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(1)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)

assert count > 0
#time.sleep(2)
for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,"input.promoCode").send_keys("rahulshettyacademy")
#driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
driver.close()



