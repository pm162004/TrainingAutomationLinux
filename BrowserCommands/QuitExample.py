from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@class='btn btn-info']").click()
time.sleep(5)

driver.quit()