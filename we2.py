

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver =webdriver.Chrome(executable_path="C:\\Users\chumbala\Desktop\web\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("abhishek")
driver.find_element_by_xpath("//input[@name='email']").send_keys("abhishekchumbalakar21@gmail.com")
#driver.find_elements_by_css_selector("input[id='inlineRadio1']").click()
#webdriver =select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@id='inlineRadio1']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
d=driver.find_element_by_class_name("alert").text
assert "success" in d