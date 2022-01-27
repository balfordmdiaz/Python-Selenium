from selenium import webdriver
from threading import Thread, Barrier

def func(threads):

    driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")
    driver.get(url)

    driver.find_element_by_id("email").send_keys("correo")
    driver.find_element_by_id("pass").send_keys("password")

    threads.wait()
    getIn = driver.find_element_by_name("login").click()

url = "https://www.facebook.com/"

num_multitask = 5

barrier = Barrier(num_multitask)

threads = []

for _ in range(num_multitask):
    i = Thread(target=func, args=(barrier,))
    i.start()
    threads.append(i)

#agregar multitareas
for i in threads:
    i.join()