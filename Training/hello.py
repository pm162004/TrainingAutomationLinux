from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
print("Hello")
time.sleep(5)
