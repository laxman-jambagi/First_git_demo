import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select #used for selecting drop down

service_obj = Service("./chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# HTML_code
# <select class="form-control" id="exampleFormControlSelect1">
#                         <option>Male</option>
#                         <option>Female</option>
#                       </select>
#
gender_elm = driver.find_element(By.ID, "exampleFormControlSelect1")

gender_drop_down = Select(gender_elm)
gender_drop_down.select_by_visible_text("Female")
time.sleep(2)
gender_drop_down.select_by_index(0)

# time.sleep(5)
# driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")


# country_opt = driver.find_element(By.XPATH, "(//select)[1]")
# country_drop_down = Select(country_opt)
# country_drop_down.select_by_value("DZA")
# print("selecting drop down is completed")

# country_opts = driver.find_elements(By.XPATH, "(//select)[1]")
# time.sleep(2)
#
# #print(country_opts)
# for country in country_opts:
#     drop = Select(country)
#     if country.text == "India":
#         drop.select_by_visible_text("India")
#         break
#
driver.close()



