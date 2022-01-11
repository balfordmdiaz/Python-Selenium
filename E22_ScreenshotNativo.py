from selenium import webdriver

driver = webdriver.Chrome(executable_path = r"C:\driverChrome\chromedriver.exe")
driver.get("https://backend.distribuidorahermanosdiaz.com/")
driver.get_screenshot_as_file("C:\\Users\\Balford\\OneDrive\\Documents\\Python-Selenium\\distribuidoraa.png")
driver.quit()