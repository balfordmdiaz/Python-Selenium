#Auto rellenar el formulario con Excel
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time

class test_case(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")

    def test_autorellenar_formulario_excel(self):
        driver = self.driver
        driver.get("http://appdistribuidorahd.test/")
        user = driver.find_element_by_id("email")   #utilizando el campo id
        user.send_keys("admin@distribuidorahd.com")  #ingresando los valores al campo
        passw = driver.find_element_by_id("password")
        passw.send_keys("XlmK0qqy+QGa")
        passw.send_keys(Keys.ENTER)
        time.sleep(3)
#
        #Ingresando a formulario de Categoria
        menu = driver.find_element_by_xpath("//*[@id='app']/nav/div/button/span").click()
        time.sleep(3)
        submenu = driver.find_element_by_xpath("/html/body/div/nav/div/div/ul/li[4]/a").click()
        time.sleep(3)
        subcatego = driver.find_element_by_xpath("/html/body/div/nav/div/div/ul/li[4]/div/a[1]").click()
        time.sleep(3)
        new_catego = driver.find_element_by_xpath("//*[@id='profile-tab']").click()
        time.sleep(3)

        filesheet = "./categorias.xlsx"
        wb = load_workbook(filesheet)
        hojas = wb.get_sheet_names()    #cargar nombres del archivo
        print(hojas)
        names = wb.get_sheet_by_name("Sheet1")  #seleccionando pagina del archivo
        wb.close()
        
        for i in range(1,6):
            categoria = names[f'A{i}']  #[f'A{i}:C{i}'][0] accesa a varias columnas
            print(categoria.value)

            #Rellenando los campos
            catego = driver.find_element_by_id("txtname")
            catego.send_keys(categoria.value)
            catego.send_keys(Keys.ENTER)
            time.sleep(3)
            print("*****    DATOS ENVIADOS  *****")
            new_categor = driver.find_element_by_xpath("//*[@id='profile-tab']").click()
            time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()