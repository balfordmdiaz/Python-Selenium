#Auto rellenar el formulario
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class test_case(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_autorellenar_formulario(self):
        driver = self.driver
        driver.get("https://backend.distribuidorahermanosdiaz.com/")
        time.sleep(3)

        with open('datos.txt') as file:
            for i, line in enumerate(file):
                usuario = (line)
                sep = ","   #separa los datos que lleven ,
                dividir = usuario.split(sep)
                try:
                    gotdata = dividir[1]
                    user = dividir[0]
                    pas = dividir[1]
                except IndexError:
                    gotdata = "null"

                print(user)
                print(pas)
                driver.find_element_by_id("email").send_keys(user)
                time.sleep(2)
                driver.find_element_by_id("password").send_keys(pas)
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='app']/main/div/div/div/div/div[2]/form/div[3]/div/button").click()
                time.sleep(3)
                file.close()


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()