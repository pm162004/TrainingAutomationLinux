from calendar import month

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
time.sleep(2)
driver.switch_to.frame(0)
# dd/mm/yyyy
# driver.find_element(By.ID,"//input[@id='datepicker']").send_keys("04/16/2025")
year = "2025"
month= "April"
day = "16"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
time.sleep(2)
