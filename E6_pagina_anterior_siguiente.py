import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class using_unittest(unittest.TestCase):

    def setUp(self):   #funciones
        options = webdriver.ChromeOptions() #escogiendo el navegador
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_pagination_back_next(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.get("http://www.youtube.com")
        time.sleep(3)
        driver.get("http://www.facebook.com")
        time.sleep(3)
        driver.back()   #regresa a la pagina anterior
        time.sleep(3)
        driver.back()   #regresa a la pagina anterior
        time.sleep(3)
        driver.forward()    #va a la siguiente pagina
        time.sleep(3)

if __name__ == '__main__':  #funcion que corre el unitest
    unittest.main()