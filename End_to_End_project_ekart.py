import time

from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("./chromedriver/chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")-getting error in on of the find element
#chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/angularpractice/')
#a[contains(@href,'shop')], #a[href*='shop']
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
time.sleep(2)
#products = driver.find_elements(By.XPATH, "//div/h4/a")
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    if product.find_element(By.XPATH,"div/h4/a").text == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()


driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary'").click()
driver.find_element(By.CSS_SELECTOR, "button[class ='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='India']")))
driver.find_element(By.XPATH,"//a[text()='India']").click()
driver.find_element(By.XPATH,'//div[@class="checkbox checkbox-primary"]').click()

driver.find_element(By.XPATH,"//input[@type='submit']").click()

success_text = driver.find_element(By.CSS_SELECTOR, "[class*='alert-success alert']").text
assert "Success! Thank you!" in success_text
print("test case pass")
print(":git xhhhh")
driver.close()

