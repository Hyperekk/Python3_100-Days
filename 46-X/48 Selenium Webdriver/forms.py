from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import keyboard

LINK = "http://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(LINK)

f_name = driver.find_element(by=By.NAME,value="fName")
l_name = driver.find_element(by=By.NAME,value="lName")
email = driver.find_element(by=By.NAME,value="email")

f_name.send_keys("Maciej")
l_name.send_keys("Kurkiuewicz")
email.send_keys("mail@gmail.com"+Keys.ENTER)

while True:
    if keyboard.is_pressed("q"):
        driver.quit()
        break



