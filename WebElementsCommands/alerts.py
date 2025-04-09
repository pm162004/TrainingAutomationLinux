from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(1.0)
# driver.find_element(By.XPATH,"//button[@id='alertBtn']").click()
# # driver.execute_script("arguments[0].click();", element)
# obj=driver.switch_to.alert
# print(obj)
# time.sleep(1.0)
# driver.find_element(By.XPATH,"//button[@id='confirmBtn']").click()
# time.sleep(1.0)
# driver.switch_to.alert.accept()
# time.sleep(1.0)

driver.find_element(By.XPATH,"//button[@id='promptBtn']").click()
time.sleep(2)
# Switch to the prompt alert
alert = driver.switch_to.alert

# Send input to the prompt alert
alert.send_keys("priya")

# Wait for a moment to observe the action
time.sleep(2)

# Accept the alert to close it
alert.accept()

# Wait to observe the result
time.sleep(2)





