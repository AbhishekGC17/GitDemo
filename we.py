from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\chumbala\Desktop\web\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
#driver.find_element_by_name("email").send_keys("abhishekgc1992@gmail.com")
driver.find_element_by_css_selector("input[name='email']").send_keys("abhishekgc1992@gmail.com")
driver.find_element_by_name("pass").send_keys("@Abhishek123")
#driver.find_element_by_name("login").click()
#driver.find_element_by_xpath().click()
button=driver.find_element_by_xpath("//button[@name='login']").click()
#driver.execute_script("arguments[0].click();", button)
print(driver.title)
print(driver.current_url)
