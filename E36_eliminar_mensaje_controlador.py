#Eliminar mensaje de automation del navegador
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class test_case(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe", options=chrome_options)
        
    def test_entrando_gmail(self):
        driver = self.driver
        driver.get("https://www.google.com/intl/es-419/gmail/about/")
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()