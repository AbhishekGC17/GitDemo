from selenium import webdriver
validateText="option 3"
driver=webdriver.Chrome(executable_path="E:\\New folder (2)\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_name("enter-name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()

alert=driver.switch_to.alert
assert validateText in alert.text

alert.accept()



