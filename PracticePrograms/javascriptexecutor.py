from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)
#getattribute to get the value of the text entered by selenium

print(driver.find_element_by_name("name").get_attribute("value"))
#to give the control to javascript(execute_script)
#to give control back to selenium (return)
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
#shopButton = driver.find_element_by_xpath("//a[contains(@href,'shop')]")
shopButton = driver.find_element_by_css_selector("a[href*='shop']")
#clicking on shop button using javascript,arguments[0] means the locator which is targetted(shopButton)
driver.execute_script('arguments[0].click();' , shopButton)
#to scroll down in selenium using javascript
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')