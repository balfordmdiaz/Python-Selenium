from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions() #escogiendo el navegador
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")  #utilizando el driver
driver.get("https://login.live.com/")   #pagina a visitar

user = driver.find_element_by_id("i0116")   #utilizando el campo id
user.send_keys("balfordmdiaz@outlook.com")  #ingresando los valores al campo
user.send_keys(Keys.ENTER)  #enviado acciones de teclados (keys)
time.sleep(3)   #tiempo utilizado al importar la libreria time

passw = driver.find_element_by_id("i0118")
passw.send_keys("Balford.2021")
passw.send_keys(Keys.ENTER)
time.sleep(3)