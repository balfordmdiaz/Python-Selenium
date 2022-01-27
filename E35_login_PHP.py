from selenium import webdriver
import keyboard
import pyautogui
import time

driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")
driver.get("http://217.182.87.241/testlink/login.php")
time.sleep(3)
keyboard.write("mi usuario")
time.sleep(3)
pyautogui.press("tab")
time.sleep(2)
keyboard.write("mi contra")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
driver.close()