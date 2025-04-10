from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
driver.maximize_window()
driver.find_element(By.ID,("username"))# to find element username
driver.find_element(By.ID,("password"))#to find the element password
time.sleep(5)
driver.close()
