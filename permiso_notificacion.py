from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions() 

options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications" : 2
})

options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options,executable_path = r"C:\driverChrome\chromedriver.exe")
# enviar argumento (1 permitiendo la notif, 2 bloquean la notif)
driver.get("https://developer.mozilla.org/es/docs/Web/API/notification")
time.sleep(3)