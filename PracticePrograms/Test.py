from selenium import webdriver

validate_text = "option 1"
driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("input#name").send_keys(validate_text)
driver.find_element_by_id("alertbtn").click()

#creating an object of the alert to access the alert pop-up and then accessing through the alert driver
#driver-is used for the html page
#alert-is used for the java script, coz you can't handle javascript page with html page
alert = driver.switch_to.alert
alert_text= alert.text
assert validate_text in alert_text
alert.accept()