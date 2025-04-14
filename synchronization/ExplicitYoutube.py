import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
Mywait = WebDriverWait(driver,10)
element = driver.find_element(By.NAME,"q")
element.send_keys("Logo")
element.submit()
Mywait.until(EC.presence_of_element_located((By.NAME,"q")))
time.sleep(4)