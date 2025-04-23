from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Set up headless mode for Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode

# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)

# Ensure the 'screenshots' directory exists
os.makedirs("screenshots", exist_ok=True)

# Navigate to a webpage
driver.get("https://www.example.com")

# Save the screenshot
driver.save_screenshot("screenshots/priya.png")
print("Headless Browser")
# Close the browser
driver.quit()
