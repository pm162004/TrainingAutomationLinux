from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
driver.execute_script('window.scrollBy(0,2000)',"")
time.sleep(2)

