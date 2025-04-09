from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(1.0)
driver.find_element(By.XPATH,"//button[@id='alertBtn']").click()
# driver.execute_script("arguments[0].click();", element)
obj=driver.switch_to.alert
print(obj)
time.sleep(1.0)



