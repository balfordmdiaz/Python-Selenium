from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")
driver.get("https://www.amazon.com/-/es/")
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.close()