from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import keyboard


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number = driver.find_element(by=By.CSS_SELECTOR,value="#articlecount a")
# number.click()

contents = driver.find_element(by=By.NAME,value="search")
contents.send_keys("Barack Obama")
contents.send_keys(Keys.ENTER)



while True:
    if keyboard.is_pressed("q"):
        driver.quit()
        break
