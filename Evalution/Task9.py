from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

wait = WebDriverWait(driver, 20)
driver.maximize_window()
# Fill out the form
driver.find_element(By.ID, "firstName").send_keys("pri")
driver.find_element(By.ID, "lastName").send_keys("modi")
driver.find_element(By.ID, "userEmail").send_keys("pri12@example.com")

driver.find_element(By.XPATH, "//label[text()='Male']").click()

driver.find_element(By.ID, "userNumber").send_keys("9876543210")

driver.find_element(By.ID, "dateOfBirthInput").click()

driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("2004")
driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("January")
driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--001') and not(contains(@class, 'outside-month'))]").click()

subjects_input = driver.find_element(By.ID, "subjectsInput")
subjects_input.send_keys("Maths")
subjects_input.send_keys(Keys.ENTER)


checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Sports']")))
driver.execute_script("arguments[0].click();", checkbox)


# Then click the checkbox
# driver.find_element(By.XPATH, "//label[text()='Sports']").click()

# driver.find_element(By.XPATH, "//label[text()='Sports']").click()

# btn1 = driver.find_element(By.XPATH, "//label[text()='Sports']")
# driver.execute_script("arguments[0].click;",btn1)

file_input = driver.find_element(By.ID, "uploadPicture")
file_path = os.path.abspath("1.png")  # Replace with your actual file path
file_input.send_keys(file_path)

uploaded_file_path = file_input.get_attribute("value")
print("Uploaded file path:", uploaded_file_path)

driver.find_element(By.ID, "currentAddress").send_keys("123 Demo Street, Adipur")

btn = driver.find_element(By.XPATH, "//label[@id='stateCity-label']")
driver.execute_script("window.scrollBy(0, 1000);", btn)

# Wait for State input to be visible and interactable
state_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
state_input.send_keys("NCR")
state_input.send_keys(Keys.ENTER)

# Wait for City input to be visible and interactable
city_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-4-input")))
city_input.send_keys("Delhi")
city_input.send_keys(Keys.ENTER)

# Submit the form
driver.find_element(By.ID, "submit").click()

# Wait and Close
time.sleep(2)
driver.quit()
