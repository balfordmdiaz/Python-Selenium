import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class bk_database(unittest.TestCase):

    def setUp(self):   #funciones
        chromeOptions = Options()
        chromeOptions.add_experimental_option("prefs", {
        "download.default_directory" : "C:\\Users\\Balford\\OneDrive\\Documents\\Distribuidora",
        })
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chromeOptions)

    def test_search(self):
        driver = self.driver
        driver.get("https://cp7048.webempresa.eu:2443/login/")
        time.sleep(3)
        user = driver.find_element(By.ID, "login")   #utilizando el campo id
        user.send_keys("distri21")  #ingresando los valores al campo
        passw = driver.find_element(By.ID, "password")
        passw.send_keys("9a4(JF#Zr9Bar2")
        passw.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.get("https://cp7048.webempresa.eu:2443/phpMyAdmin/") #dirigir a base de datos
        time.sleep(3)
        submenu = driver.find_element(By.XPATH, "//*[@id='topmenucontainer']/nav/button/span").click()
        time.sleep(1)
        export = driver.find_element(By.XPATH, "//*[@id='topmenu']/li[4]/a")
        export.click()
        time.sleep(1)
        download = driver.find_element(By.ID, "buttonGo").click()
        time.sleep(3)

    def tearDown(self): #cerramos el driver
        self.driver.close()


if __name__ == '__main__':  #funcion que corre el unitest
    unittest.main()