import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class bk_database(unittest.TestCase):

    def setUp(self):   #funciones
        options = webdriver.ChromeOptions() #escogiendo el navegador
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")


    def test_search(self):
        driver = self.driver
        driver.get("https://distri21-cp5038.wordpresstemporal.com:2083/cpsess0604349005/3rdparty/phpMyAdmin/db_structure.php?server=1&db=distri21_distribuidorahd")
        user = driver.find_element_by_id("user")   #utilizando el campo id
        user.send_keys("distri21")  #ingresando los valores al campo
        passw = driver.find_element_by_id("pass")
        passw.send_keys("9a4(JF#Zr9Bar2")
        passw.send_keys(Keys.ENTER)
        time.sleep(1)
        export = driver.find_element_by_xpath("//*[@id='topmenu']/li[5]/a")
        export.click()
        time.sleep(1)
        download = driver.find_element_by_xpath("//*[@id='buttonGo']")
        download.click()
        time.sleep(3)

    def tearDown(self): #cerramos el driver
        self.driver.close()


if __name__ == '__main__':  #funcion que corre el unitest
    unittest.main()