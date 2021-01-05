from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\\New folder (2)\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()
