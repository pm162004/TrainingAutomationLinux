from select import select

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://safarr-admin-dev.webelight.co.in/sign-in")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("admin@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Admin@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3.0)
driver.forward()
driver.get("https://safarr-admin-dev.webelight.co.in/truth-or-truth")
time.sleep(3.0)
driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div/div/div/main/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/div/span[2]/button").click()
time.sleep(3.0)

element = driver.find_element(By.XPATH,"(//*[contains(text(),'Please Select')])[1]")
driver.execute_script("arguments[0].click();", element)


time.sleep(3.0)

driver.close()
