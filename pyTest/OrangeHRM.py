from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_script():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

def test_login1():

    driver.find_element(By.NAME, "username").send_keys("admin")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("1234")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(4)
    driver.close()

def test_login():
    driver.back()
    time.sleep(1)

    name = driver.find_element(By.NAME, "username")
    name.send_keys(Keys.CONTROL,"a")
    name.send_keys(Keys.ENTER)
    name.send_keys("Admin")
    time.sleep(2)
    passw = driver.find_element(By.NAME, "password")
    passw.send_keys(Keys.CONTROL, "a")
    passw.send_keys(Keys.ENTER)
    passw.send_keys("admin123")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(2)


