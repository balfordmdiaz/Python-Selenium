#Captura el error
import unittest
from selenium import webdriver
import time

class suite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_assertEqual(self):
        driver = self.driver
        driver.get("http://www.google.com/")
        pageTitle = driver.title
        self.assertEqual("Gogle", pageTitle, "El titulo de la pagina no es igual")
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()