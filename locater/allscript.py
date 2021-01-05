import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver =webdriver.Chrome(executable_path="E:\\New folder (2)\chromedriver.exe")
#driver.implicitly_wait("6")
driver.get("https://rahulshettyacademy.com/angularpractice/shop")

driver.find_element_by_css_selector("a[href*='shop']").click()
elements=driver.find_elements_by_xpath("//div[@class='card h-100']")

for element in elements:
    x=element.find_element_by_xpath("div/h4/a").text
    if x == "Blackberry":
        element.find_element_by_xpath("div/button").click()
driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("Ind")

wait=WebDriverWait(driver,6)
wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT,"India")))
driver.find_element_by_partial_link_text("India").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
d =driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you" in d

driver.save_screenshot("full.png")
print(driver.page_source)
driver.delete_cookie()
time.sleep(6)
driver.close()