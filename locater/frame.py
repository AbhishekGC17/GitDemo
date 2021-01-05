import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\\New folder (2)\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("my name is abhi")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
print("display:",driver.title)
time.sleep(4)
driver.close()

