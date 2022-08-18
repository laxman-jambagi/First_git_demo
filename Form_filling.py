import time
from typing import Set

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import  By

#create a service object by passing the chrodriver path in Service() class
# relative path proividing the path first create a Chromedriver directory in current project and then place the chromedriver.exe inside it.
service_obj = Service("./Chromedriver/chromedriver.exe")
#create a chrome driver class. it will accept the service= service_obj

driver= webdriver.Chrome(service=service_obj)
driver.maximize_window()
# invoke the browser with URL by using get method
driver.get("https://rahulshettyacademy.com/angularpractice/")
#find the element on web page by using .find_element() and find_elements() methonds, first arguments it takes by( locators) and 2nd argument is values

# locators- locators are used to identify the web element on webpage
# ID, NAME, CLASS_NAME, TAG_NAME, LINK_TEXT, PARTIAL_LINK_TEXT, CSS_SELECTOR, XPATH
#CSS_SELECTOR Syntax-Tagname#id, #id, tag name.class value, tagname[Attribute:'value'], contain text in the tag
#tagname[atrtibute*=text], starting the text tagname[attribute^='value', ending the text tagname[attribut$='value'
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Laxman Jambagi")
driver.find_element(By.NAME, 'email').send_keys("laxman@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.CLASS_NAME,"form-check-input").click()
driver.find_element(By.ID,"inlineRadio2").click()
#driver.find_element(By.NAME,"bday").click()

driver.find_element(By.XPATH,  "//input[@type='submit']").click()

msg = driver.find_element(By.CLASS_NAME,"alert-dismissible").text
#print(msg)

assert "success" in msg

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear() #clear method is used to clear the text filed

driver.close()