from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome() #Launch The Browser
driver.get("https://demoqa.com/alerts")  # Open the website
driver.maximize_window()


btn = driver.find_element(By.XPATH, "//button[@id='alertButton']")
print(btn.text)
# ========== Handle Regular Alert ==========
driver.find_element(By.ID, "alertButton").click()

    # Wait for the alert to appear
WebDriverWait(driver, 10).until(EC.alert_is_present())

    # Switch to alert
alert = driver.switch_to.alert
# Get alert text
print("Alert text:", alert.text)

    # Accept the alert
alert.accept()

btn.click()
time.sleep(4)








