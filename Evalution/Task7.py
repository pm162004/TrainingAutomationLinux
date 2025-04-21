from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()



driver.get("https://dev.webelight.co.in/contact-us")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

driver.execute_script('window.scrollBy(0,500)',"")


btn = driver.find_element(By.XPATH, "//img[@alt='logo']")


driver.execute_script("window.scrollBy(0, 2300);",btn)
time.sleep(2)
checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Blog']")))
driver.execute_script("arguments[0].click();", checkbox)

time.sleep(2)