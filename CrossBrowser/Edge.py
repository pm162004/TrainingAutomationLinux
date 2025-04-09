from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(5)
driver.close()
