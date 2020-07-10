import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
#count = driver.find_elements_by_xpath("//div[@class='products']/div")
#output = len(count)
#assert output == 3
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for i in buttons:
    i.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
#driver.find_element_by_xpath("//div[@class='cart-preview active']/div/button").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
#print(driver.find_element_by_css_selector("span.promoInfo").text)
cupon= driver.find_element_by_css_selector("span.promoInfo").text
print(cupon)
