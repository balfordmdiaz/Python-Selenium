import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class test_case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")
        
    def test_manejando_ventanas(self):
        self.driver.get("https://www.google.com/intl/es/gmail/about/#")
        time.sleep(3)
        next = self.driver.find_element_by_xpath("/html/body/main/div[1]/div/div/div/div/div[3]/div[1]/a/span[1]")
        next.click()
        print(self.driver.current_window_handle)
        time.sleep(3)

        handles=self.driver.window_handles

        for handle in handles:
            self.driver.switch_to.window(handle)
            print(self.driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()