
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://safarr-admin-dev.webelight.co.in/sign-in")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("admin@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Admin@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0)
driver.forward()
driver.get("https://safarr-admin-dev.webelight.co.in/truth-or-truth")
time.sleep(3.0)   # select the truth or truth menu
driver.get("https://safarr-admin-dev.webelight.co.in/truth-or-truth")
time.sleep(3.0)   # select the truth or truth menu
toggles = driver.find_elements(By.CLASS_NAME, "switcher-toggle")  # finds all
toggles[0].click()
driver.find_element(By.XPATH,"(//button[normalize-space()='Confirm'])[1]").click()
time.sleep(2) # CONFIRM
button = driver.find_element(By.XPATH, "(//button)[5]")
button.click()
time.sleep(3.0)   # Edit Button