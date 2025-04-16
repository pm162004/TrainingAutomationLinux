
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.implicitly_wait(10)


#take the screenshorts
driver.save_screenshot('/home/web-h-028/PycharmProjects/TrainingAutomation/Evalution/1.png')
time.sleep(3.0)  # Wait for the page to load