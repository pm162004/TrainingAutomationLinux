from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome() #Launch The Browser
driver.get("https://demoqa.com/alerts")  # Open the website
driver.maximize_window()


btn = driver.find_element(By.XPATH, "//button[@id='alertButton']")
alert = driver.switch_to.alert

btn.click()
time.sleep(4)
