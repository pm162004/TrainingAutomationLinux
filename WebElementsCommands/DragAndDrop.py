import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
time.sleep(2)
Seoul=driver.find_element(By.XPATH,'//*[@id="box5"]')
country=driver.find_element(By.XPATH,'//*[@id="box106"]')
time.sleep(2)
action=ActionChains(driver)
time.sleep(2)
action.drag_and_drop(Seoul,country).perform()
time.sleep(2)