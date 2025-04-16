from selenium import webdriver
import time
driver = webdriver.Chrome() #Launch The Browser
driver.get("https://example.com")  # Open the website
driver.maximize_window()
print(driver.title)
time.sleep(2)
driver.close()