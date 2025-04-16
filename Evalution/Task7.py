from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# from SafarAdminPanel.Advertisements import error_message

# Init WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open the Site
driver.get("https://dev.webelight.co.in/contact-us")
driver.maximize_window()

# Give the page time to load
time.sleep(2)

driver.execute_script('window.scrollBy(0,500)',"")
time.sleep(2)