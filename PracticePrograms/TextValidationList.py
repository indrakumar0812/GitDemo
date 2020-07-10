import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list = []
list2 = []
driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(8)
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
# driver.find_element_by_class_name("search-button").click()
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for i in buttons:
    list.append(i.find_element_by_xpath("parent::div/parent::div/h4").text)
    i.click()

print(list)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'input.promoCode')))

vegname = driver.find_elements_by_css_selector("p.product-name")

for i in vegname:
    list2.append(i.text)

print(list2)

assert list == list2

driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'span.promoInfo')))
print(driver.find_element_by_css_selector("span.promoInfo").text)
