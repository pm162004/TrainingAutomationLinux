from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Wait for up to 10 seconds
driver.get("https://omayo.blogspot.com/")
element = driver.find_element(By.ID,"alert2")
