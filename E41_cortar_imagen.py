import unittest
from selenium import webdriver
from PIL import Image
from io import BytesIO
import time

class test_case(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_descargando(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        time.sleep(3)
        img = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/img")
        imgFound = img.location
        size = img.size
        saveImg = driver.get_screenshot_as_png()
        img2 = Image.open(BytesIO(saveImg))
        left = imgFound['x']
        top = imgFound['y']
        right = imgFound['x'] + size ['width']
        bottom = imgFound['y'] + size ['height']
        img2 = img2.crop((left, top, right, bottom))
        img2.save('mi_logo.png')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()