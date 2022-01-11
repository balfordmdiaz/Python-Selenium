import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class bk_database(unittest.TestCase):

    def setUp(self):   #funciones
        chromeOptions = Options()
        chromeOptions.add_experimental_option("prefs", {
        "download.default_directory" : "C:\\Users\\Balford\\OneDrive\\Documents\\Distribuidora",
        })
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe", chrome_options=chromeOptions)


    def test_search(self):
        driver = self.driver
        driver.get("https://distri21-cp5038.wordpresstemporal.com:2083/cpsess0604349005/3rdparty/phpMyAdmin/db_structure.php?server=1&db=distri21_distribuidorahd")
        user = driver.find_element_by_id("user")   #utilizando el campo id
        user.send_keys("distri21")  #ingresando los valores al campo
        passw = driver.find_element_by_id("pass")
        passw.send_keys("9a4(JF#Zr9Bar2")
        passw.send_keys(Keys.ENTER)
        time.sleep(1)
        export = driver.find_element_by_xpath("//*[@id='topmenu']/li[5]/a")
        export.click()
        time.sleep(1)
        download = driver.find_element_by_xpath("/html/body/div[4]/form/div[7]/input").click()
        time.sleep(3)

    def tearDown(self): #cerramos el driver
        self.driver.close()


if __name__ == '__main__':  #funcion que corre el unitest
    unittest.main()