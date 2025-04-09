from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
driver.execute_script("arguments[0].click()",driver.find_element(By.ID,"RESULT_CheckBox-8_0"))
driver.execute_script("arguments[0].click()",driver.find_element(By.ID,"RESULT_CheckBox-8_5"))
driver.execute_script("arguments[0].click()",driver.find_element(By.ID,"RESULT_CheckBox-8_6"))
time.sleep(4)
driver.close()