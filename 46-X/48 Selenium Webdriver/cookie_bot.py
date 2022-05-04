from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import keyboard

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(2)
cookie = driver.find_element(by=By.ID,value="bigCookie")

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

a = True
while a:
    cookie.click()
    if keyboard.is_pressed("q"):
            driver.quit()
            a = False
    if time.time() > timeout:
        upgrades = driver.find_elements(by=By.CSS_SELECTOR,value="#upgrades div")
        products = driver.find_elements(by=By.CSS_SELECTOR,value="#products div")

        for up in upgrades:
            if 'enabled' in up.get_attribute('class').split():
                up.click()
                #nie dziala


        # for pro in reversed(products):
        #     if 'enabled' in pro.get_attribute('class').split():
        #         time.sleep(1)
        #         pro.click()


        timeout = time.time() + 5