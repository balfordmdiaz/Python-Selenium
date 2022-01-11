from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")
driver.get("https://www.w3schools.com/html/default.asp")
time.sleep(3)
#acceder a todos los cookies de la pagina
all_cookies = driver.get_cookies()

print(all_cookies)