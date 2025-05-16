from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()  # or use Edge(), Firefox(), etc.
driver.maximize_window()

# Open a webpage with scrollbars (replace with your target URL)
driver.get("https://www.w3schools.com/css/css_overflow.asp")
time.sleep(2)

# --- Vertical Scroll ---
# Scroll down by 1000 pixels
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(2)

# Scroll up by 500 pixels
driver.execute_script("window.scrollBy(0, -500);")
time.sleep(2)

# --- Horizontal Scroll ---
# For horizontal scroll, you need a horizontally scrollable element.
# Example: scroll a div with overflow-x set

# Find the scrollable element
scroll_element = driver.find_element(By.XPATH, "//div[@class='w3-white w3-padding notranslate w3-example']")

# Scroll right by 300 pixels
driver.execute_script("arguments[0].scrollLeft += 300;", scroll_element)
time.sleep(2)

# Scroll left by 150 pixels
driver.execute_script("arguments[0].scrollLeft -= 150;", scroll_element)
time.sleep(2)

# Close browser
driver.quit()
