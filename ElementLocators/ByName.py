from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.NAME,"session_key")# to find element username
driver.find_element(By.NAME,"session_password")#to find the element password
time.sleep(5)

