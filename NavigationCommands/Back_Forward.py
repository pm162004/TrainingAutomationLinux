from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=o3tYiyE_OXE")
driver.maximize_window()
driver.get("https://www.webelight.com/")
driver.forward()
time.sleep(5)