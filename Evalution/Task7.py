from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re


driver = webdriver.Chrome()
driver.implicitly_wait(20)


driver.get("https://dev.webelight.co.in/contact-us")
driver.maximize_window()


time.sleep(2)

# driver.execute_script('window.scrollBy(0,500)',"")


btn = driver.find_element(By.XPATH, "//img[@alt='logo']")


driver.execute_script("window.scrollBy(0, 2300);",btn)
time.sleep(2)
btn1 = driver.find_element(By.XPATH,"//a[contains(text(),'Blog')]")
driver.execute_script("arguments[0].click;",btn1)
time.sleep(2)