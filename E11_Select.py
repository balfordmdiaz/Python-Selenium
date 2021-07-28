from functools import partialmethod
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class using_select(unittest.TestCase):

    def setUp(self):   #funciones
        options = webdriver.ChromeOptions() #escogiendo el navegador
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")
    
    def test_select(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(3)
        selec = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
        option = selec.find_elements_by_tag_name("option")
        time.sleep(3)
        for opt in option: #con el for recorre todos los valores que se encuentran en el select
            print("Los valores son: %s" % opt.get_attribute("value"))
            opt.click()
            time.sleep(1)
        seleccionar = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("8")
        time.sleep(3)

    def tearDown(self): #cerramos el driver
        self.driver.close()


if __name__ == '__main__':  #funcion que corre el unitest
    unittest.main()

