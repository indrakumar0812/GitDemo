from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
assert driver.find_element_by_css_selector("input#displayed-text").is_displayed()
driver.find_element_by_css_selector("input#hide-textbox").click()
assert not driver.find_element_by_css_selector("input#displayed-text").is_displayed()