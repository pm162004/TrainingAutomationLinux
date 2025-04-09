from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from ElementLocators.ById import placeholder_element
# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the LinkedIn login page
driver.get("https://www.linkedin.com/login")
driver.maximize_window()

# Corrected line: use the attribute selector for the 'aria-label'
placeholder_element = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Email or phone']")

# Fetch the placeholder text using the get_attribute method


print(f"Placeholder text: {placeholder_element}")

time.sleep(2)
driver.close()
