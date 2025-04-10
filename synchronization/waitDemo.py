from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
element = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search for Vegetables and Fruits']").send_keys("priya")
driver.execute_script("arguments[0]",element)
time.sleep(2)