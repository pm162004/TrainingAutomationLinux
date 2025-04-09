from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the LinkedIn login page
driver.get("https://www.linkedin.com/login")
driver.maximize_window()

# Wait for the input field to be visible before interacting with it
wait = WebDriverWait(driver, 10)
placeholder_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Email or phone']")))



# Alternatively, check the value of other attributes
aria_label_value = placeholder_element.get_attribute("aria-label")
print(f"Aria-label: '{aria_label_value}'")

# Wait for a few seconds before closing
time.sleep(2)

# Close the driver
driver.close()
