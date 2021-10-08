from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#argumentos que hacer que corran a segundo plano
chrome_options = Options()
chrome_options.add_argument("--headless")

palabra_busqueda = "selenium"

options = webdriver.ChromeOptions() #escogiendo el navegador
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(chrome_options=chrome_options,options=options,executable_path=r"C:\driverChrome\chromedriver.exe")
driver.get("https://www.google.com/")
time.sleep(3)

busqueda = driver.find_element_by_name("q")
busqueda.send_keys(palabra_busqueda)
time.sleep(3)

for i in range(1,11):
    elementos = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/ul/li["+str(i)+"]/div/div[2]/div[1]/span").text
    print(palabra_busqueda + elementos)
driver.close()
