from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")

driver.implicitly_wait(5)

# Click the "Single Iframe" tab (just to ensure it's active)
driver.find_element(By.XPATH, "//a[text()='Single Iframe ']").click()

# Switch to the single iframe
iframe = driver.find_element(By.ID, "singleframe")
driver.switch_to.frame(iframe)

# Interact with the input field inside iframe
input_box = driver.find_element(By.TAG_NAME, "input")
input_box.send_keys("Hello iframe!")

# Switch back to main page
driver.switch_to.default_content()

time.sleep(2)
driver.quit()
