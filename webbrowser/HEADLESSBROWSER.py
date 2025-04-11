from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU (optional, sometimes needed)

# Initialize the WebDriver with the headless option
driver = webdriver.Chrome(options=chrome_options)

# Open a website (no GUI will be shown)
driver.get("https://selectorshub.com/iframe-scenario/")

# Perform actions or assertions (e.g., print page title)
print("Page title:", driver.title)

# Close the browser session
driver.quit()
