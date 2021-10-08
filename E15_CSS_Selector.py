from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions() #escogiendo el navegador
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")
driver.get("https://www.w3schools.com/html/default.asp")
time.sleep(3)
content = driver.find_element_by_css_selector('a.w3-btn')  #agregar a. el selector
content.click()
time.sleep(3)