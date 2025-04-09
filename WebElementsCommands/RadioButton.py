from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
status = driver.find_element(By.ID,"RESULT_RadioButton-7_0").is_selected()
print(status)

driver.execute_script("arguments[0].click()",driver.find_element(By.ID,"RESULT_RadioButton-7_1"))
#driver.execute_script("arguments[1].click()",driver.find_element(By.ID,"RESULT_RadioButton-7_0"))
status = driver.find_element(By.ID,"RESULT_RadioButton-7_1").is_selected()
print(status)
driver.maximize_window()
time.sleep(4)
driver.close()