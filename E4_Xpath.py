import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class using_unittest(unittest.TestCase):

    def setUp(self):   #funciones
        options = webdriver.ChromeOptions() #escogiendo el navegador
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("https://login.live.com/")
        time.sleep(3)
        buscar_por_xpath = driver.find_element_by_xpath("//*[@id='i0116']")
        time.sleep(3)
        buscar_por_xpath.send_keys("balfordmdiaz@outlook.com")
        buscar_por_xpath.send_keys(Keys.ENTER)
        #buscar_por_xpath.send_keys("Facebook", Keys.ARROW_DOWN)
        time.sleep(3)

    def tearDown(self): #cerramos el driver
        self.driver.close()

if __name__ == '__main__':  #funcion que corre el unitest
    unittest.main()


