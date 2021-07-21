import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class using_unittest(unittest.TestCase):

    def setUp(self):   #funciones
        options = webdriver.ChromeOptions() #escogiendo el navegador
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")


    def test_search(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)   #buscamos el titulo
        element = driver.find_element_by_name("q") #utilizando el campo nombre (buscador)
        element.send_keys("selenium")
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontro el elemento:" not in driver.page_source  #verificacion si no encuentra el titulo a buscar


    def tearDown(self): #cerramos el driver
        self.driver.close()


if __name__ == '__main__':  #funcion que corre el unitest
    unittest.main()