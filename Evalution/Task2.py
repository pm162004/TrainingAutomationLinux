from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome() #Launch The Browser
driver.get("https://the-internet.herokuapp.com/login")  # Open the website
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
driver.close()