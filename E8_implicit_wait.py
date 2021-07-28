import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class using_unittest(unittest.TestCase):

    def setUp(self):   #funciones
        options = webdriver.ChromeOptions() #escogiendo el navegador
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_using_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #segundos
        driver.get("http://www.backend.distribuidorahermanosdiaz.com")
        myDynamicElement = driver.find_element_by_name("email") #obtener componentes

if __name__ == '__main__':  #funcion que corre el unitest
    unittest.main()