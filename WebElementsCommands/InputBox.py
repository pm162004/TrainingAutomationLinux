from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/login.html")
driver.find_element(By.ID,"email").send_keys("priya@gmail.com")
driver.find_element(By.ID,"passwd").send_keys("priya@123")

driver.maximize_window()
time.sleep(1)
driver.close()