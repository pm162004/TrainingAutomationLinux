from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

# ===== Click the Register button without filling any fields =====
driver.find_element(By.ID, "register-button").click()
time.sleep(1)

# ===== Capture validation messages =====
first_name_error = driver.find_element(By.ID, "FirstName-error").text
last_name_error = driver.find_element(By.ID, "LastName-error").text
email_error = driver.find_element(By.ID, "Email-error").text

confirm_password_error = driver.find_element(By.ID, "ConfirmPassword-error").text

# ===== Assert expected error messages =====
assert first_name_error == "First name is required.", "First name error message mismatch"
assert last_name_error == "Last name is required.", "Last name error message mismatch"
assert email_error == "Email is required.", "Email error message mismatch"

assert confirm_password_error == "Password is required.", "Confirm password error message mismatch"

print("Empty field validations passed.")

# ===== Enter invalid email format =====
driver.find_element(By.ID, "Email").send_keys("invalidemail")
driver.find_element(By.ID, "register-button").click()
time.sleep(1)

invalid_email_error = driver.find_element(By.ID, "Email-error").text

# ===== Assert invalid email format error =====
assert invalid_email_error == "Wrong email", "Invalid email error message mismatch"

print("Invalid email format validation passed.")

# ===== Enter mismatching passwords =====
driver.find_element(By.ID, "Password").send_keys("Password123")
driver.find_element(By.ID, "ConfirmPassword").send_keys("DifferentPassword")
driver.find_element(By.ID, "register-button").click()
time.sleep(1)

password_mismatch_error = driver.find_element(By.ID, "ConfirmPassword-error").text

# ===== Assert password mismatch error =====
assert password_mismatch_error == "The password and confirmation password do not match.", "Password mismatch error message mismatch"

print("Password mismatch validation passed.")

# ===== Close the browser =====
time.sleep(3)
driver.quit()
