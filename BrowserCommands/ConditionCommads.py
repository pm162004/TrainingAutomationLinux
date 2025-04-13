from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
time.sleep(2)
search = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display status : ",search.is_displayed())
print("Display enabled : ",search.is_enabled())

time.sleep(2)
selection = driver.find_element(By.XPATH,"//input[@id='gender-male']")
print(selection.is_selected())
selection.click()
print(selection.is_selected())