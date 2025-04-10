from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/") # get geeksforgeeks.org

action = ActionChains(driver) # create action chain object

# perform the operation with keys up and down
action.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(1)
action.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(1)
action.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(1)
action.send_keys(Keys.ARROW_UP).perform()
