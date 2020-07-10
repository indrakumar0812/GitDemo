from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_xpath("//form[contains(@class,'ng-untouched')]/div[1]/input").send_keys("Indrasen")
driver.find_element_by_name("email").send_keys("abc@gmail.com")
driver.find_element_by_id("exampleCheck1").click()
sel = Select(driver.find_element_by_id("exampleFormControlSelect1"))
sel.select_by_visible_text("Male")
driver.find_element_by_css_selector("input[type='submit']").click()
alertText = driver.find_element_by_css_selector("div[class*='alert-success']").text

assert ("Success!" in alertText)