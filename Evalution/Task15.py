from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome() #Launch The Browser
driver.get("https://rahulshettyacademy.com/AutomationPractice/")  # Open the website
driver.maximize_window()
driver.switch_to.frame("courses-iframe")
driver.find_element(By.XPATH, "//div[@class='top-right clearfix']//div[1]").click()

time.sleep(4)
