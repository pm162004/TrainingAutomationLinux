from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(1)
driver.close()
driver.quit()