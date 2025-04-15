from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# from SafarAdminPanel.Advertisements import error_message

# Init WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open the Site
driver.get("https://dev.webelight.co.in/contact-us")
driver.maximize_window()

# Give the page time to load
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

# Send keys to the full name input field
driver.find_element(By.ID, "name").send_keys("Test")

# Wait for 2 seconds
time.sleep(2)

# Send keys to the email input field
driver.find_element(By.ID, "email").send_keys("Test123@gmail.com")

# Send keys to the Country Code field
Country = driver.find_element(By.XPATH, "//div[@title='India: + 91']")
# Wait for the country option to be visible and clickable
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@title='India: + 91']"))
)
Country.click()

search = driver.find_element(By.XPATH, "//input[@placeholder='search']")
search.send_keys("In")
search.send_keys(Keys.ENTER)
time.sleep(2)

# Wait for 2 seconds
time.sleep(2)

# Send keys to the phone input field
driver.find_element(By.ID, "phone").send_keys("9999999999")

companyName = "SimForm"

# Send keys to the Company Name input field
driver.find_element(By.ID, "companyName").send_keys(companyName)


message = "Automation testing practice is on."
# Send keys to the message input field
driver.find_element(By.ID, "message").send_keys(message)


time.sleep(2)

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3.0) #

driver.close()