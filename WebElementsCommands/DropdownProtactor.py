from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# drop = driver.find_element(By.ID,"exampleFormControlSelect1")
# time.sleep(2)
# driver.find_element(By.XPATH,"//option[normalize-space()='Female']").click()
# time.sleep(5)

drop = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
drop.select_by_index(0)
drop.select_by_visible_text("Female")
time.sleep(5)