from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(20)
wait = WebDriverWait(driver, 10)

# ===== Fill Name and Email =====
driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Doe")
driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")

# ===== Select Gender (Radio Button) =====
driver.find_element(By.XPATH, "//label[text()='Male']").click()

# ===== Fill Mobile Number =====
driver.find_element(By.ID, "userNumber").send_keys("9876543210")

# ===== Set Date of Birth (1st Jan 1999) =====
driver.find_element(By.ID, "dateOfBirthInput").click()

# Select Year
driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1999")
# Select Month
driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("January")
# Select Day
driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--001') and not(contains(@class, 'outside-month'))]").click()

# ===== Select Subjects =====
subjects_input = driver.find_element(By.ID, "subjectsInput")
subjects_input.send_keys("Maths")
subjects_input.send_keys(Keys.ENTER)

# ===== Select Hobbies (Checkboxes) =====
driver.find_element(By.XPATH, "//label[text()='Sports']").click()
driver.find_element(By.XPATH, "//label[text()='Reading']").click()

# ===== File Upload =====
file_input = driver.find_element(By.ID, "uploadPicture")
file_path = os.path.abspath("1.png")  # Replace with your actual file path
file_input.send_keys(file_path)

# Verify file uploaded (prints value)
uploaded_file_path = file_input.get_attribute("value")
print("Uploaded file path:", uploaded_file_path)

# ===== Enter Current Address =====
driver.find_element(By.ID, "currentAddress").send_keys("123 Demo Street, Testville")

# ===== Select State and City (Dropdowns) =====
driver.execute_script("window.scrollBy(0, 500);")

# State
state_input = driver.find_element(By.ID, "react-select-3-input")
state_input.send_keys("NCR")
state_input.send_keys(Keys.ENTER)

# City
city_input = driver.find_element(By.ID, "react-select-4-input")
city_input.send_keys("Delhi")
city_input.send_keys(Keys.ENTER)

# ===== Submit the Form =====
driver.find_element(By.ID, "submit").click()

# ===== Wait and Close =====
time.sleep(5)
driver.quit()
