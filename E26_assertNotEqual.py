#Captura el cambio especificado
import unittest
from selenium import webdriver
import time

class suite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_assertNotEqual(self):
        driver = self.driver
        driver.get("http://www.google.com/")
        pageTitle = driver.title
        time.sleep(2)
        self.assertNotEqual("Google", pageTitle, "El titulo de la pagina es igual")
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()