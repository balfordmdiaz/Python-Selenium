import unittest
import HtmlTestRunner
from selenium import webdriver
import time

class suite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")
    
    def test_busqueda(self):#poner la cantidad de test case que queramos
        self.driver.get("http://www.google.com/")
        self.busqueda = self.driver.find_element_by_name("q")
        self.busqueda.send_keys("selenium")
        self.busqueda.submit()
        time.sleep(3)
    
    def test_busqueda_youtube(self):
        self.driver.get("http://www.youtube.com/")
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Resultado de mi test plan'))