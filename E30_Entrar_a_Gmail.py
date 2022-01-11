import unittest
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class test_case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\driverChrome\geckodriver.exe")
        
    def test_entrando_gmail(self):
        self.driver.get("https://www.google.com/intl/es-419/gmail/about/")
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/header/div/div/div/a[2]").click()
        time.sleep(3)
        user = self.driver.find_element_by_xpath("//*[@id='identifierId']").send_keys("balfordm21@gmail.com")
        time.sleep(3)
        next = self.driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/span").click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()