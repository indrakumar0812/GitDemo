import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

str ="You double clicked me!!!, You got to be kidding me"
driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://jqueryui.com/")
actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_link_text("JS Foundation")).perform()
actions.move_to_element(driver.find_element_by_link_text("Leadership")).click().perform()
driver.close()

driver1 = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver1.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
wait = WebDriverWait(driver, 8)
#wait.until(expected_conditions.element_to_be_clickable((By.ID, "double-click")))
wait.until(expected_conditions.presence_of_element_located((By.ID, "double-click")))
actions.double_click(driver1.find_element_by_id("double-click")).perform()
alert = driver1.switch_to.alert
assert str == alert.text
alert.accept()


