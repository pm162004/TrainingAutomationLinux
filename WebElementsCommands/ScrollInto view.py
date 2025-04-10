from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

driver.switch_to.frame(0)
scrollDown = driver.find_element(By.ID,"singleFileInput")
# scrollDown.location_once_scrolled_into_view
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView();",scrollDown)
time.sleep(2)