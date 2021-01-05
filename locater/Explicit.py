import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="E:\\New folder (2)\chromedriver.exe")
driver.implicitly_wait(8)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
time.sleep(3)
count= len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
product =driver.find_elements_by_xpath("//div[@class='product-action']/button")
for x in product:
  x.click()

driver.find_element_by_css_selector("a[class='cart-icon']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
#wait =WebDriverWait(driver,8)
#wait.until(expected_conditions.presence_of_all_elements_located(By.CLASS_NAME, "promoCode"))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_class_name("promoBtn").click()
#wait.until(expected_conditions.presence_of_all_elements_located(By.CLASS_NAME, "promoInfo"))
print(driver.find_element_by_class_name("promoInfo").text)
print(driver.current_url)
time.sleep(9)
driver.close()