from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=chrome_options)
"""this exercise to get the upcoming events in pyhon.org the name and the time and put it in a dictionary"""
driver.get("https://www.python.org/")
upcoming_events={}
event_times=driver.find_elements(By.CSS_SELECTOR,".event-widget li time")
event_names=driver.find_elements(By.CSS_SELECTOR, ".event-widget  li a")
for n in range(len(event_times)):
    upcoming_events[n]={
        "time":event_times[n].text,
        "name":event_names[n].text
    }
print(upcoming_events)

driver.quit()

