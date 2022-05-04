from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&keywords=python%20junior")
driver.maximize_window()
time.sleep(2)
log_in = driver.find_element(by=By.CLASS_NAME,value="nav__button-secondary")
log_in.click()
time.sleep(1)
email = driver.find_element(by=By.NAME,value="session_key")
password = driver.find_element(by=By.NAME,value="session_password")

email.send_keys(input("E-mail: "))
password.send_keys(input("Password: "))

send = driver.find_element(by=By.CSS_SELECTOR,value=".login__form_action_container button")
send.click()
time.sleep(2)

job_offers = driver.find_elements(by=By.CSS_SELECTOR,value=".job-card-container")

for job in job_offers[0:8]:
    job.click()
    time.sleep(1)
    try:
        driver.find_element(by=By.CLASS_NAME,value="jobs-save-button").click()
    except NoSuchElementException:
        continue