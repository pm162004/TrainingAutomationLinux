from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
driver.maximize_window()
time.sleep(5)
element = driver.find_element(By.CSS_SELECTOR,"[type='email']").send_keys('priya')

driver.execute_script("arguments[0];",element)
time.sleep(5)
