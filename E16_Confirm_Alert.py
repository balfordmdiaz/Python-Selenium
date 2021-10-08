from selenium import webdriver
import time

options = webdriver.ChromeOptions() #escogiendo el navegador
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")
driver.get("file:///C:/Users/Balford/OneDrive/Documents/Python-Selenium/confirm_alert.html")
time.sleep(3)
confirm_alert = driver.find_element_by_name("confirmar_alert")
confirm_alert.click()
time.sleep(3)
confirm_alert = driver.switch_to_alert()
confirm_alert.dismiss() #dismiss or accept
time.sleep(3)
driver.close()