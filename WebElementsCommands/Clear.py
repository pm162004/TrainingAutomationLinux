from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time
driver.get("https://practice.automationtesting.in/")
driver.maximize_window()
dr = driver.find_element(By.XPATH,"//input[@type='email']").click()
dr.clear
time.sleep(5)

driver.quit()