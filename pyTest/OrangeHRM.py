from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_script():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

def test_login():
    time.sleep(1)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("admin123")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(4)
    driver.close()
