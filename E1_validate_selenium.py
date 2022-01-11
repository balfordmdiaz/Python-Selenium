from selenium import webdriver
import time

#options = webdriver.ChromeOptions() 
#options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path = r"C:\driverChrome\chromedriver.exe")
driver.get("http://python.org")
time.sleep(5)