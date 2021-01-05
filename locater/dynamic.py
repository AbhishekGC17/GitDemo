import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\\New folder (2)\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
cities =driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print (len(cities))
for city in cities:
    if city.text =="India":
        city.click()
        break

assert driver.find_element_by_id("autosuggest").get_attribute("value")== "India"