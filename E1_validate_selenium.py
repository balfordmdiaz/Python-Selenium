from selenium import webdriver
import time

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options,executable_path = r"C:\driverChrome\chromedriver.exe")
driver.get("http://python.org")
time.sleep(5)