import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
#print(products)
#//div[@class='card h-100']/div/h4/a

for i in products:
    productName = i.find_element_by_xpath("div/h4/a").text
    print(productName)
    if productName == "Blackberry":
        #Add item to cart
        i.find_element_by_xpath("div[2]/button").click()
   # if productName == "Samsung Note 8":
        #i.find_element_by_xpath("div[2]/button").click()
driver.find_element_by_css_selector("a[class*= 'btn-primary']").click()
final = driver.find_element_by_xpath("//h4[@class='media-heading']/a").text

assert productName == final

driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[contains(@class,'checkbox-primary')]").click()
driver.find_element_by_css_selector("input[type='submit']").click()
successText = driver.find_element_by_css_selector("div[class*='alert-succes']").text

assert "Success! Thank you!" in successText

driver.get_screenshot_as_file("screen.png")