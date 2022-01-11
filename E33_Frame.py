import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class test_case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")
        
    def test_nuevo_frame(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        click1 = driver.find_element_by_id("gbwa")
        time.sleep(3)
        click1.click()
        time.sleep(3)
        driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[3]/iframe"))
        time.sleep(3)
        click2 = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/ul[1]/li[4]/a/div/span")
        click2.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()