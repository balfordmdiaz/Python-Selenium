from selenium import webdriver

driver = webdriver.Firefox(executable_path=r"C:\driverChrome\geckodriver.exe")
driver.get("https://coderbyte.com")
driver.close()