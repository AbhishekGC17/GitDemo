from selenium import webdriver
from selenium.webdriver import ActionChains

driver =webdriver.Chrome(executable_path="E:\\New folder (2)\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
t=driver.find_element_by_id("mousehover")
action=ActionChains(driver)
action.move_to_element(t).perform()
td=driver.find_element_by_link_text("Reload")
action.move_to_element(td).click().perform()
driver.close()