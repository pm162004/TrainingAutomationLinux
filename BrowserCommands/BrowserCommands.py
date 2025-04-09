from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time
driver.get("https://stage.app.navodayatransport.com/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(5)