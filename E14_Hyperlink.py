from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions() #escogiendo el navegador
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")
driver.get("https://www.w3schools.com/")
time.sleep(5)
find_link = driver.find_element_by_link_text('Learn PHP')
find_link.click()
time.sleep(5)