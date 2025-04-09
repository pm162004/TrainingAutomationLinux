from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time
driver.get("https://www.google.co.in/")
driver.maximize_window()
time.sleep(5)
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)
driver.back()
driver.get("https://www.amazon.co.in/")
driver.maximize_window()
time.sleep(5)
driver.back()