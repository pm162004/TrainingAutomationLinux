from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
time.sleep(2)

actions = ActionChains(driver) # driver pass as a parameter
