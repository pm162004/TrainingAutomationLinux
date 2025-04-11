from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/login.html")
driver.maximize_window()
driver.find_element(By.ID,"email").send_keys("112i@gmail.com")
driver.find_element(By.ID,"passwd").send_keys("123456789")
driver.find_element(By.ID,"SubmitLogin").click()
time.sleep(1.0)
driver.close()
