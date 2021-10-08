import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class using_unittest(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.read('configuration.ini')
        config.sections()
        getexplorer = config['General']['chrome']
        self.page = config['Pages']['page']
        self.driver = webdriver.Chrome(executable_path=getexplorer)

    def test_using_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #segundos
        driver.get(self.page)
        myDynamicElement = driver.find_element_by_name("q")
            

if __name__ == '__main__':  #funcion que corre el unitest
    unittest.main()


