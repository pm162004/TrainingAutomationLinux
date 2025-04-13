
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://safarr-admin-dev.webelight.co.in/sign-in")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("")
driver.find_element(By.NAME,"password").send_keys("")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0) # blank inputs

adminUname = driver.find_element(By.NAME,"email")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("admin@gmail.com")
adminUpass = driver.find_element(By.NAME,"password")
adminUpass.send_keys(Keys.CONTROL,"a")
adminUpass.send_keys(Keys.DELETE)
adminUpass.send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0) # wrong password

adminUname = driver.find_element(By.NAME,"email")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("admin1@gmail.com")
adminUpass = driver.find_element(By.NAME,"password")
adminUpass.send_keys(Keys.CONTROL,"a")
adminUpass.send_keys(Keys.DELETE)
adminUpass.send_keys("Admin@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0) # wrong email

adminUname = driver.find_element(By.NAME,"email")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("admin1@gmail.com")
adminUpass = driver.find_element(By.NAME,"password")
adminUpass.send_keys(Keys.CONTROL,"a")
adminUpass.send_keys(Keys.DELETE)
adminUpass.send_keys("Admin@12")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0) # wrong email password

adminUname = driver.find_element(By.NAME,"email")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("admin@gmail.com")
adminUname = driver.find_element(By.NAME,"password")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("Admin@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0)
driver.forward()