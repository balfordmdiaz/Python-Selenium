import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains #acceso a hardware de nuestro equipo
import time

class test_case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")
        
    def test_mouse_dobleclick(self):
        self.driver.get("https://backend.distribuidorahermanosdiaz.com/login/")
        time.sleep(3)
        rclick = self.driver.find_element_by_xpath("/html/body/div/main/div/div/div/div/div[2]/form/div[3]/div/button")
        actions = ActionChains(self.driver)
        actions.context_click(rclick).perform()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()