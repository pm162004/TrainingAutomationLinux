from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"singleFileInput").send_keys("/home/web-h-028/Downloads/responsive.png")
time.sleep(2)
