import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Toggle_switch(unittest.TestCase):

    def setUp(self):   #funciones
        options = webdriver.ChromeOptions() #escogiendo el navegador
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options,executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_toggle(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        time.sleep(3)
        toggle = driver.find_element_by_xpath("//*[@id='main']/label[3]/div")
        toggle.click()
        time.sleep(3)
        toggle.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__': 
    unittest.main()

    