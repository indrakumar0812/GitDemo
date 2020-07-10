from selenium import webdriver
from selenium.webdriver import ActionChains

str ="You double clicked me!!!, You got to be kidding me"
driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://jqueryui.com/")
actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_link_text("JS Foundation")).perform()
actions.move_to_element(driver.find_element_by_link_text("Leadership")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
actions.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
assert str == alert.text
alert.accept()
