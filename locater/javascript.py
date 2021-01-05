import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\\New folder (2)\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/#top")
driver.find_element_by_id("name").send_keys("abhi")
print(driver.find_element_by_id("name").text)
print(driver.find_element_by_id("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("enter-name")[0].value'))
time.sleep(4)
driver.close()