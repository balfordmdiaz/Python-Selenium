from selenium import webdriver
import time

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options,executable_path = r"C:\driverChrome\chromedriver.exe")
driver.get("file:///C:/Users/Balford/OneDrive/Documents/Python-Selenium/prompalert.html")
time.sleep(2)
alert = driver.find_element_by_name("prompt_alert")
alert.click()
time.sleep(3)
alert = driver.switch_to_alert()
alert.send_keys("Balford")
time.sleep(3)
alert.accept() #accion de aceptar
# alert.dismiss() #accion de cancelar
time.sleep(3)
driver.close()