from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.get("https://www.nutriag.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"jet-menu-item-21886").click()
time.sleep(3)
element = driver.find_element(By.XPATH,"(//*[contains(text(),'Our Team')])[1]")
driver.execute_script("arguments[0].click();", element)
time.sleep(2)
driver.back()
element2 = driver.find_element(By.XPATH,"(//*[contains(text(),'Join Us')])[1]")

driver.execute_script("arguments[0].click();", element2)