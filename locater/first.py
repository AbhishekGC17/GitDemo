import time

from selenium import webdriver
list = []
list2 = []
driver=webdriver.Chrome(executable_path="E:\\New folder (2)\chromedriver.exe")
driver.implicitly_wait(8)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
time.sleep(3)
count= len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
product =driver.find_elements_by_xpath("//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4
for x in product:
  list.append(x.find_element_by_xpath("parent::div/parent::div/h4").text)
  x.click()
print(list)



driver.find_element_by_css_selector("a[class='cart-icon']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()


veggies =driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    list2.append(veg.text)

print(list2)
originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_class_name("promoBtn").click()
discountAmount = driver.find_element_by_css_selector(".discountAmt").text
print(int(originalAmount))
print(float(discountAmount))
#assert float(discountAmount) == int(originalAmount)
print(driver.find_element_by_class_name("promoInfo").text)
time.sleep(9)
driver.close()