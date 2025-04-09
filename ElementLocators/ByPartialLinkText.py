from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time
driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,'Sign').click()
time.sleep(5)
driver.close()
