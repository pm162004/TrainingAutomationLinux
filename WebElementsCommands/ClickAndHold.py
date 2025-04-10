from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
time.sleep(2)

actions = ActionChains(driver) # driver pass as a parameter

link = driver.find_element(By.PARTIAL_LINK_TEXT, "DSA to Development")

actions.click_and_hold(link).perform()
time.sleep(2)
actions.release(link).perform()
