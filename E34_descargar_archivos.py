import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class test_case(unittest.TestCase):
    
    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_experimental_option("prefs", {
        "download.default_directory" : "C:\\DriverChrome",
        })
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe", chrome_options=chromeOptions)

    def test_descargando(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")
        time.sleep(3)
        driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/iframe"))
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/p[2]/a").click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()