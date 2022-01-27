import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

class test_case(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_descargando(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        time.sleep(3)
        radiob = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[4]")
        time.sleep(3)
        try:
            radiob.click()
            time.sleep(3)
        except WebDriverException as e:
            print('No se ejecuto el evento del radio button')   #imprime esto para falso
            print(e)                                            #imprime esto para verdadero
            time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()