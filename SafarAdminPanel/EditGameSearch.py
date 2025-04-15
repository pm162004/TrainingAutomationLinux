from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Start the driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://safarr-admin-dev.webelight.co.in/sign-in")
driver.maximize_window()

# Login with blank inputs (this is an invalid login case)
driver.find_element(By.NAME,"email").send_keys("")
driver.find_element(By.NAME,"password").send_keys("")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0) # blank inputs

# Assert that an error message appears due to blank inputs
error_message = driver.find_element(By.XPATH, "//div[contains(text(),'Email is required.') or contains(text(),'Password is required.')]")
print("Error message text:", error_message.text)

# Assert that the error message contains the expected text
assert "Email is required" in error_message.text or "Password is required" in error_message.text, f"Error message not found: {error_message.text}"

adminUname = driver.find_element(By.NAME,"email")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("admin@gmail.com")
adminUpass = driver.find_element(By.NAME,"password")
adminUpass.send_keys(Keys.CONTROL,"a")
adminUpass.send_keys(Keys.DELETE)
adminUpass.send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0) # wrong password

# Check if error message is displayed
error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Invalid credentials Please try again with valid credentials ⚠')]")  # Change to actual error text if different
print("Error message text:", error_message.text)
assert error_message.is_displayed(), "Error message not found for wrong Password"

adminUname = driver.find_element(By.NAME,"email")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("admin1@gmail.com")
adminUpass = driver.find_element(By.NAME,"password")
adminUpass.send_keys(Keys.CONTROL,"a")
adminUpass.send_keys(Keys.DELETE)
adminUpass.send_keys("Admin@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0) # wrong email

# Check if error message is displayed
error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Invalid credentials Please try again with valid credentials ⚠')]")  # Change to actual error text if different
print("Error message text:", error_message.text)
assert error_message.is_displayed(), "Error message not found for wrong email"

adminUname = driver.find_element(By.NAME,"email")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("admin1@gmail.com")
adminUpass = driver.find_element(By.NAME,"password")
adminUpass.send_keys(Keys.CONTROL,"a")
adminUpass.send_keys(Keys.DELETE)
adminUpass.send_keys("Admin@12")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0) # wrong email password

# Check if error message is displayed
error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Invalid credentials Please try again with valid credentials ⚠')]")  # Change to actual error text if different
print("Error message text:", error_message.text)
assert error_message.is_displayed(), "Error message not found for wrong email and password"

# Login with correct credentials
adminUname = driver.find_element(By.NAME,"email")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("admin@gmail.com")
adminUname = driver.find_element(By.NAME,"password")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("Admin@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0)
driver.forward()

# Assert that login was successful by checking the URL or dashboard presence
print("Current URL:", driver.current_url)  # Print the current URL for debugging
assert "users" in driver.current_url, "Login failed, dashboard not found"

# Check if Successful message is displayed
Successful_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Logged in successfully.')]")  # Change to actual error text if different
print("Successful text:", Successful_message.text)
assert Successful_message.is_displayed(), "Successful message is not found after login"


# Now navigating to the Truth or Truth section
driver.get("https://safarr-admin-dev.webelight.co.in/truth-or-truth")
time.sleep(3.0)  # Wait for the page to load


# Further operations like toggle switches, translating, etc., can also be asserted similarly
# Example: Assert toggle state is changed after click
toggle = driver.find_elements(By.CLASS_NAME, "switcher-toggle")
toggle[0].click()



# Closing the browser at the end
driver.find_element(By.XPATH,"(//button[normalize-space()='Confirm'])[1]").click()
time.sleep(1) # CONFIRM

# Edit a question and change language
driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]/div[1]/span[2]/button[1]").click()
time.sleep(3.0)  # Edit Button

# Open language dropdown and select English
driver.find_element(By.XPATH, "(//div[@class='select__control css-15bhs5i-control'])[1]").click()
time.sleep(3.0)  # open the dropdown
sel = driver.find_element(By.XPATH, "(//*[contains(text(),'English')])[1]")
driver.execute_script("arguments[0].click();", sel)

time.sleep(3.0)  # select the English
driver.find_element(By.XPATH, "(//button[normalize-space()='Submit'])[1]").click()
time.sleep(3.0)  # submit button
input_element = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Question'])[1]")
 # This clears any existing text in the input field
input_element.click()
input_element.send_keys(Keys.CONTROL + "a")  # or Keys.COMMAND + "a" on macOS
input_element.send_keys(Keys.DELETE)

# Then send new text
random_number = random.randint(100000, 999999)
Search2 = "Test User "+str(random_number)
input_element.send_keys(Search2)

time.sleep(3) # write the question
driver.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click()
time.sleep(3) # Click the save button

# Check if Successful message is displayed
Successful_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Question has been updated successfully.')]")  # Change to actual error text if different
print("Successful text:", Successful_message.text)
assert Successful_message.is_displayed(), "Successful message is not found after update the new user"

# Check if error message is displayed
try:
    error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Question Already Exists ⚠')]")
    print("Error message text:", error_message.text)
    assert error_message.is_displayed(), "Error message not found for 'Question already Exists'"
except NoSuchElementException:
    print("Error message not found.")


#Search the Game

search = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search.send_keys(Search2)
search.send_keys(Keys.ENTER)

time.sleep(3.0)  # Wait for the page to load

#take the screenshorts
driver.save_screenshot('/home/web-h-028/PycharmProjects/TrainingAutomation/SafarAdminPanel/TestUser.png')
time.sleep(3.0)  # Wait for the page to load