import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:\\New folder (2)\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
check =driver.find_elements_by_xpath("//input[@type='checkbox']")
for box in check:
    box.click()
    assert box.is_selected()
time.sleep(2)
driver.close()