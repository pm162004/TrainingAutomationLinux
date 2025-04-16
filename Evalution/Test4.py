from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() #Launch The Browser
driver.get("https://dev.webelight.co.in/")  # Open the website
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(4)
ele = driver.find_element(By.LINK_TEXT, 'About Us')
driver.execute_script("arguments[0].click();",ele)

time.sleep(4)
