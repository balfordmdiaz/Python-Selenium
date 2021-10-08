from selenium import webdriver
import time

options = webdriver.ChromeOptions() #escogiendo el navegador
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(3)

valor = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr").text   #al dejar solo tr me trae toda la informacion
print(valor)

rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr")) #cant de filas
col = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th")) #cant de columnas

print(rows)
print(col)

for n in range(2, rows+1):
    for b in range(1, col+1):
        dato = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text    #+str()+ convierte el numero en caracter
        print(dato, end='           ')  #se agrega los tab para que s emuestre ordenado el listado
    print()