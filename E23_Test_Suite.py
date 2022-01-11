import unittest
from selenium import webdriver
import time

class suite(unittest.TestCase):
    def setUp(self):
        #self.cdriver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")
        self.edriver = webdriver.Ie(executable_path=r"C:\driverChrome\IEDriverServer.exe")
    
    #def test_busqueda(self):#poner la cantidad de test case que queramos
    #    self.cdriver.get("http://www.google.com/")
    #    self.busqueda = self.cdriver.find_element_by_name("q")
    #    self.busqueda.send_keys("selenium")
    #    self.busqueda.submit()
    #    time.sleep(3)
    
    def test_usando_internet_explorer(self):
        self.edriver.get("http://www.google.com/")
        time.sleep(3)

    def tearDown(self):
        #self.cdriver.close()
        self.edriver.close()

if __name__ == '__main__':
    unittest.main()