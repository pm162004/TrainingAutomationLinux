from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://login.salesforce.com/")
driver.maximize_window()
driver.find_element(By.ID,'username').send_keys('priya')
driver.find_element(By.NAME,'pw').send_keys('priya@123')
driver.find_element(By.XPATH,'//*[@id="Login"]').click()
driver.find_element(By.LINK_TEXT,'Forgot Your Password?').click()
time.sleep(5)
driver.close()
