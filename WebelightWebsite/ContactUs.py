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

# Send keys to the full name input field
driver.find_element(By.ID, "name").send_keys("Test")

# Retrieve the value of the full name field after sending the keys
fullName = driver.find_element(By.ID, "name").get_attribute("value")

# Check if fullName is not None and matches the pattern
if fullName:
    assert re.match(r"^[A-Za-z\s]+$", fullName), "Validation Failed for Fullname"
    print("Validation Passed for Fullname")
else:
    print("Full Name cannot be None")

# Wait for 2 seconds
time.sleep(2)

# Send keys to the email input field
driver.find_element(By.ID, "email").send_keys("Test123@gmail.com")

# Retrieve the value of the email field after sending the keys
email = driver.find_element(By.ID, "email").get_attribute("value")

# Check if email is valid
if email:
    assert re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email), "Validation Failed for Email"
    print("Validation Passed for Email")
else:
    print("Email cannot be None")

# Wait for 2 seconds
time.sleep(2)

# Send keys to the Country Code field
Country = driver.find_element(By.XPATH, "//div[@title='India: + 91']")
# Wait for the country option to be visible and clickable
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@title='India: + 91']"))
)
Country.click()

time.sleep(2)
search = driver.find_element(By.XPATH, "//input[@placeholder='search']")
search.send_keys("In")
search.send_keys(Keys.ENTER)
time.sleep(2)

# Wait for 2 seconds
time.sleep(2)

# Send keys to the phone input field
driver.find_element(By.ID, "phone").send_keys("9999999999")

# Retrieve the value of the phone field after sending the keys
phone = driver.find_element(By.ID, "phone").get_attribute("value")

# Print the phone number for debugging purposes
print("Entered Phone Number:", phone)

# Check if the phone number is valid using a phone number regex pattern
if phone:
    phone_pattern = r"^\+91\s\d{5}-?\d{5}$"  # India phone number with optional hyphen
    if re.match(phone_pattern, phone):
        print("Validation Passed for Phone")
    else:
        print(f"Validation Failed for Phone: {phone}")
else:
    print("Phone cannot be None")


# Wait for 2 seconds
time.sleep(2)

companyName = "SimForm"

# Send keys to the Company Name input field
driver.find_element(By.ID, "companyName").send_keys(companyName)

# Retrieve the value of the Company Name field after sending the keys
phone = driver.find_element(By.ID, "companyName").get_attribute("value")



# Check if company name is empty
assert companyName.strip(), 'Company name is required.'

# Check if length is between 3 and 100 characters
assert 3 <= len(companyName) <= 100, 'Company name must be between 3 and 100 characters.'

# Check if the company name matches the allowed characters
assert re.match(r'^[A-Za-z0-9\s\.\-\&]+$', companyName), 'Invalid characters in company name.'

# If all assertions pass, this will be printed
print('Valid:', companyName.strip())

time.sleep(2)

message = "Automation testing practice is on."
# Send keys to the message input field
driver.find_element(By.ID, "message").send_keys(message)

# Check if message is empty
assert message.strip(), 'message is required.'
print('Valid:', message.strip())

time.sleep(2)

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3.0) #

driver.close()