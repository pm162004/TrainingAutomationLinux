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


# Assert the presence of the "Add Question" button
add_question_button = driver.find_element(By.XPATH,"(//*[contains(text(),'Add Question')])[1]")
assert add_question_button.is_displayed(), "Add Question button not found"

# Add a new question
driver.execute_script("arguments[0].click();",add_question_button)
time.sleep(3.0)

input_element = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Question'])[1]")
input_element.click()
input_element.send_keys(Keys.CONTROL + "a")
input_element.send_keys(Keys.DELETE)
random_number = random.randint(100000, 999999)
Search2 = "New User " + str(random_number)
input_element.send_keys(Search2)
time.sleep(3)  # wait for typing

driver.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click()
time.sleep(1)  # Click the save button



# Assert that the new question is saved
question_text = driver.find_element(By.XPATH, "(//span[contains(text(),'New User')])[1]")
print("question message text:", question_text.text)
assert "New User" in question_text.text, "New Question was not saved correctly"

# Check if Successful message is displayed
Successful_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Question has been added successfully.')]")  # Change to actual error text if different
print("Successful text:", Successful_message.text)
assert Successful_message.is_displayed(), "Successful message is not found after add the new user"

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
driver.save_screenshot('/home/web-h-028/PycharmProjects/TrainingAutomation/SafarAdminPanel/NewUser.png')
time.sleep(3.0)  # Wait for the page to load