from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time
driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'Sign in').click()
time.sleep(5)
driver.close()
