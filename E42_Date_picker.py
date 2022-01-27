import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class test_case(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_descargando(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.edestinos.com/")
        time.sleep(3)

        #origen
        departureCity = driver.find_element_by_xpath("//*[@id='departureRoundtrip0']")
        departureCity.send_keys("Managua, Augusto C. Sandino, Nicaragua (MGA)")
        time.sleep(2)
        departureCity.send_keys(Keys.TAB)

        #destino
        arrivalCity = driver.find_element_by_xpath("//*[@id='arrivalRoundtrip0']")
        arrivalCity.send_keys("Miami (Todos los Aeropuertos), Florida, Estados Unidos (MIAM)")
        time.sleep(2)
        arrivalCity.send_keys(Keys.TAB)
        time.sleep(2)

        #fechaida
        datepick1 = driver.find_element_by_xpath("//*[@id='departureDateRoundtrip0']").click()
        upMonth = driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/a[2]/span")
        upMonth.click()
        upMonth2 = driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/a[2]/span")
        upMonth2.click()
        getDay = driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[7]/a").click()
        time.sleep(3)

        #fechavuelta
        datepick2 = driver.find_element_by_xpath("//*[@id='departureDateRoundtrip1']").click()
        getDay2 = driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/table/tbody/tr[5]/td[4]/a").click()
        time.sleep(3)

        #pasajeros
        persons = driver.find_element_by_xpath("//*[@id='multiQsfFlights']/form/section[2]/div[2]/fieldset[1]/div[1]").click()
        time.sleep(3)
        plusp = driver.find_element_by_xpath("/html/body/div[24]/div/div[2]/div[1]/div/a[2]/i").click()
        time.sleep(3)

        #aplicar
        btnaplicar = driver.find_element_by_xpath("/html/body/div[24]/div/div[2]/div[1]/div/a[2]/i")
        btnaplicar.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()