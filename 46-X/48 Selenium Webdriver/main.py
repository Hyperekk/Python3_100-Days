from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org/")
event_times_s = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events_s = driver.find_elements(By.CSS_SELECTOR, ".event-widget a")  

events = [item.text for item in events_s[1::]]
event_times_s = [f"{item.text}" for item in event_times_s]

s = {}

for i in range(len(events)):
    s[events[i]] = event_times_s[i]

print(s)


    


driver.quit()