from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# from SafarAdminPanel.Advertisements import error_message

# Init WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open the Site
driver.get("https://dev.webelight.co.in/contact-us")
driver.maximize_window()

# Give the page time to load
time.sleep(2)

driver.execute_script('window.scrollBy(0,500)',"")
time.sleep(2)
# Submit the form using the submit() method
form = driver.find_element(By.XPATH, "//button[@type='submit']")  # Adjust with the actual form's ID
form.submit()

error_message = driver.find_element(By.XPATH,"//p[normalize-space()='Full name is required.']")
print("Error message text:", error_message.text)
assert "Full name is required." in error_message.text,f"Error message not found: {error_message.text}"
# Give the page time to load
time.sleep(2)

error_message = driver.find_element(By.XPATH,"//p[normalize-space()='Please enter a valid email address.']")
print("Error message text:", error_message.text)
assert "Please enter a valid email address." in error_message.text,f"Error message not found: {error_message.text}"
# Give the page time to load
time.sleep(2)

error_message = driver.find_element(By.XPATH,"//p[normalize-space()='Phone number is required.']")
print("Error message text:", error_message.text)
assert "Phone number is required." in error_message.text,f"Error message not found: {error_message.text}"
# Give the page time to load
time.sleep(2)
# Close the browser
