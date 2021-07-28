import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class using_unittest(unittest.TestCase):

    def setUp(self):   #funciones
        options = webdriver.ChromeOptions() #escogiendo el navegador
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_Creando_Cliente(self):
        driver = self.driver
        driver.get("http://appdistribuidorahd.test/")
        user = driver.find_element_by_id("email")   #utilizando el campo id
        user.send_keys("admin@distribuidorahd.com")  #ingresando los valores al campo
        passw = driver.find_element_by_id("password")
        passw.send_keys("XlmK0qqy+QGa")
        passw.send_keys(Keys.ENTER)
        time.sleep(3)
        menu = driver.find_element_by_xpath("//*[@id='app']/nav/div/button/span")
        menu.click()
        time.sleep(3)
        subclient = driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul/li[3]/a")
        subclient.click()
        time.sleep(3)
        new_client = driver.find_element_by_xpath("//*[@id='profile-tab']")
        new_client.click()
        time.sleep(3)
        nombre = driver.find_element_by_id("txtname")
        nombre.send_keys("Lionel Messi")
        phone = driver.find_element_by_id("txttelefono")
        phone.send_keys("85023445")
        depart = driver.find_element_by_id("txtdepart")
        depart.send_keys("Rosario, Argentina")
        time.sleep(3)
        depart.send_keys(Keys.ENTER)
        time.sleep(3)
        buscador = driver.find_element_by_xpath("//*[@id='table-client_filter']/label/input")
        buscador.send_keys("Lionel Messi")
        time.sleep(3)
        view_newclient = driver.find_element_by_xpath("//*[@id='table-client']/tbody/tr/td[1]")
        view_newclient.click()
        time.sleep(5)


    def tearDown(self): #cerramos el driver
        self.driver.close()


if __name__ == '__main__':  #funcion que corre el unitest
    unittest.main()