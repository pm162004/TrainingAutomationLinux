from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the target URL
driver.get("https://testautomationpractice.blogspot.com/")

# Maximize the window
driver.maximize_window()

# Find and click the button that triggers the prompt alert
driver.find_element(By.XPATH, "//button[@id='promptBtn']").click()

# Wait for the prompt alert to appear
time.sleep(2)

# Switch to the prompt alert
alert = driver.switch_to.alert

# Send your custom text to the prompt input field
custom_text = "Priya"  # Change this to your custom text
alert.send_keys(custom_text)
print(f"Sending text to alert: {custom_text}")
alert.send_keys(custom_text)

# Wait a moment to observe the action
time.sleep(2)

# Accept the alert (click 'OK')
alert.accept()

# Wait to observe the result
time.sleep(2)

# Close the browser window
driver.quit()
