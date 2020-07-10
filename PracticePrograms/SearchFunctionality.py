import time

from selenium import webdriver

list1 = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
list2 = []
driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector(".search-keyword").send_keys("ber")
time.sleep(5)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))

print(count)

veg = driver.find_elements_by_css_selector("h4.product-name")
for i in veg:
    list2.append(i.text)

print(list2)

assert list2 == list1