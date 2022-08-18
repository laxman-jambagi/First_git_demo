import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("./chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
#find the Autosuggest drop down
#by ID
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
#By CSS Selector
# driver.find_element(By.CSS_SELECTOR,"#autosuggest").send_keys("indi")
# #By XPATH
# driver.find_element(By.XPATH, "//input[@ID ='autosuggest']").send_keys("Ind")

#find the list of countries in the dropdown by using find_elements()

countries = driver.find_elements(By.CSS_SELECTOR, "li[class = 'ui-menu-item'] a")
print(len(countries))
print(type(countries))
i=0
for country in countries:
    if country.text == "India":
        country.click()
        break

#print(driver.find_elemet(By.ID, "autosuggest").text)# .text method will not retrive the dynamically types text through scripts

print(driver.find_element(By.ID,"autosuggest").get_attribute('value'))
#.get_attribute method will retrive the dynamically enterd text on text filed
#in get_attribute we need to pass the 'value' parameter , after dynamically enter the text the value property will get updated in html dom

assert driver.find_element(By.ID,"autosuggest").get_attribute('value') == "India"
#if both the condition are true asser true also true test case passs
# if any of the condition fales assert false is false and it will throws an assertion error

driver.close()










