from selenium import webdriver
import time

#Siempre verificar vercion del driver y explorador
#https://selenium-release.storage.googleapis.com/index.html
driver = webdriver.Ie(executable_path=r"C:\driverChrome\IEDriverServer.exe")
driver.get("http://www.google.com.ni")
time.sleep(3)
driver.close()