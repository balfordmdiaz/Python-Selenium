import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Radio_Button(unittest.TestCase):

    def setUp(self):   #funciones
        options = webdriver.ChromeOptions() #escogiendo el navegador
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_radio_button(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        time.sleep(5)
        radiob = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[4]")
        radiob.click()
        time.sleep(3)
        radiob = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[3]")
        radiob.click()
        time.sleep(3)

    def tearDown(self): #cerramos el driver
        self.driver.close()


if __name__ == '__main__':  #funcion que corre el unitest
    unittest.main()
