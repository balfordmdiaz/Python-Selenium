import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class test_case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")
        
    def test_manejando_ventanas(self):
        self.driver.get("https://mdbootstrap.com/plugins/jquery/file-upload/")
        time.sleep(3)
        self.driver.find_element_by_id("customFile").send_keys("C:\\Users\\Balford\\Downloads\\Selenium_Logo-1.png")
        time.sleep(3)
        user = self.driver.find_element_by_xpath("//*[@id='identifierId']").send_keys("balfordm21@gmail.com")
        time.sleep(3)
        user = self.driver.send_keys("")
        


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()