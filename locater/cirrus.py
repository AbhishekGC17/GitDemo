import time

from selenium import webdriver
chromeoption=webdriver.ChromeOptions()
chromeoption.add_argument("--ignore_certificate-error")
driver =webdriver.Chrome(executable_path="E:\\New folder (2)\chromedriver.exe",options=chromeoption)
driver.get("https://15.118.14.123/#/login")
driver.implicitly_wait(30)
valu = "Admin123"
#driver.find_element_by_id("details-button").click()
#driver.find_element_by_id("proceed-link").click()
driver.find_element_by_xpath("//input[@id='hp-login-user']").send_keys("Abhishek")
driver.find_element_by_xpath("//input[@id='hp-login-password']").send_keys(valu)
driver.find_element_by_xpath("//button[@id='hp-login-button']").click()
driver.find_element_by_xpath("//span[text()='Manage Systems and other HW']").click()
#driver.find_element_by_xpath("//div[@id='hp-search-input']/input").send_keys("DL")
time.sleep(6)
driver.close()


