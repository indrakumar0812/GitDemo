from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

str = "You double clicked me!!!, You got to be kidding me"
driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.ID, "double-click")))
actions = ActionChains(driver)
actions.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
assert str == alert.text
alert.accept()
driver.close()