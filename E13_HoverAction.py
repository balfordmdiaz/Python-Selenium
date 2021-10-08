from selenium import webdriver
from selenium.webdriver import ActionChains #para manipular el mouse
import time

options = webdriver.ChromeOptions() #escogiendo el navegador
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")
driver.get("https://www.google.com/")
time.sleep(3)
elem = driver.find_element_by_link_text("Privacidad")

hover = ActionChains(driver).move_to_element(elem)
hover.perform()
time.sleep(5)

