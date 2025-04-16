from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

# Typing text
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Keyboard Interaction Examples")

# Submitting form with Enter key
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# Navigating with Tab and selecting address bar
ActionChains(driver).send_keys(Keys.TAB * 3).perform()
time.sleep(1)

# Scroll down with Page Down, then up with Page Up
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
ActionChains(driver).send_keys(Keys.PAGE_UP).perform()
time.sleep(1)

# Refreshing the page with F5
ActionChains(driver).send_keys(Keys.F5).perform()
time.sleep(2)

# Typing in a new query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(Keys.DELETE)


# Typing text
search_box.send_keys("Keyboard Shortcuts in Selenium")

# Select All (Ctrl+A), Copy (Ctrl+C), Clear, Paste (Ctrl+V)
search_box.send_keys(Keys.CONTROL, 'a')
search_box.send_keys(Keys.CONTROL, 'c')
search_box.clear()
search_box.send_keys(Keys.CONTROL, 'v')

time.sleep(2)

# Close browser
driver.quit()
