import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class using_unittest(unittest.TestCase):

    def setUp(self):   #funciones
        options = webdriver.ChromeOptions() #escogiendo el navegador
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_change_window(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.execute_script("window.open('');")   #script de python que abre otra ventana
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])   #se posiciona en la otra ventana
        driver.get("http://distribuidorahermanosdiaz.com")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])   #se devuelve a la primera ventana
        time.sleep(3)

if __name__ == '__main__':  #funcion que corre el unitest
    unittest.main()