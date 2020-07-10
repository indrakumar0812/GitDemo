from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
#alert.dismiss()
alert.accept()