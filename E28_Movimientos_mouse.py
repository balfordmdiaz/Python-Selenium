import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class test_case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")
        
    def test_movimientos_mouse(self):
        self.driver.get("https://www.w3schools.com/")
        time.sleep(3)
        mouse_mov = self.driver.find_element_by_xpath("//*[@id='navbtn_tutorials']")
        mouse_mov2= self.driver.find_element_by_xpath("//*[@id='nav_tutorials']/div/div/div[2]/a[1]")
        movimiento=ActionChains(self.driver)
        movimiento.move_to_element(mouse_mov).move_to_element(mouse_mov2).click().perform()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()