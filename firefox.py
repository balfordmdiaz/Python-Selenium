from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://coderbyte.com")
driver.close()