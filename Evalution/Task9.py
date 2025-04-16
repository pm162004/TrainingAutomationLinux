from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os



driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

time.sleep(2)

    # Fill First Name and Last Name
driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Doe")

    # Fill Email
driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")

    # Select Gender (Radio)
driver.find_element(By.XPATH, "//label[text()='Male']").click()

    # Fill Mobile Number
driver.find_element(By.ID, "userNumber").send_keys("1234567890")

    # Set Date of Birth to 1st Jan 1999
dob_input = driver.find_element(By.ID, "dateOfBirthInput")
dob_input.click()
time.sleep(1)
dob_input.send_keys(Keys.CONTROL + "a")  # Select all text
dob_input.send_keys("01 Jan 1999")
dob_input.send_keys(Keys.ENTER)

    # Upload a file
file_path = os.path.abspath("sample_file.txt")  # Ensure this file exists in the same folder
driver.find_element(By.ID, "uploadPicture").send_keys(file_path)

    # Verify file upload (check the value attribute)
uploaded_file = driver.find_element(By.ID, "uploadPicture").get_attribute("value")
print(f"Uploaded file path: {uploaded_file}")

    # Select Hobbies (Checkbox)
driver.find_element(By.XPATH, "//label[text()='Sports']").click()

    # Select State and City (Dropdown)
driver.execute_script("window.scrollBy(0, 300);")  # Scroll down for dropdown visibility
driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.ENTER)

driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.ENTER)

    # Submit the form
driver.find_element(By.ID, "submit").click()

time.sleep(3)
driver.quit()

