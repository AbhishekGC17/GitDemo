from selenium import webdriver

driver =webdriver.Chrome(executable_path="C:\\Users\chumbala\Desktop\web\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=eu")
driver.find_element_by_css_selector("#username").send_keys("Abhishek")
driver.find_element_by_css_selector("#password").send_keys("Abc")
d = driver.find_element_by_css_selector("div[id='usernamegroup'] lable").text

driver.find_element_by_css_selector("#Login").click()
#driver.find_element_by("Forgot Your Password?").click()