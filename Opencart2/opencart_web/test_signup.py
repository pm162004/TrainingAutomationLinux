import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Opencart2.opencart_setup.config import config
from Opencart2.opencart_setup.randomeString import random_string_generator
import Opencart2.constant
from Opencart2.constant import creds, validation_assert
from Opencart2.constant import error
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType
# from selenium.webdriver.chrome.service import Service as ChromeService

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# Only run with the latest Chrome version
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get(config.WEB_URL)
email = config.EMAIL
password = config.PASSWORD
wait = WebDriverWait(driver, 25)

def MyAccountPage():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='My Account']")))

def register():
    return wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))

def login_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']")))

def click_logout_button():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//aside[@id='column-right']//a[normalize-space()='Logout']")))


def register_continue():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Continue']")))

def signup():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Continue']")))

def signup_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='list-group-item'][normalize-space()='Register']")))

def first_name_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'First Name must be between 1 and 32 characters!')]")))

def last_name_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]")))

def email_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'E-Mail Address does not appear to be valid!')]")))

def exist_email_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")))

def mobile_no_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]")))

def set_password_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Password must be between 4 and 20 characters!')]")))

def confirm_password_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Password confirmation does not match password!')]")))

def agree_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")))

def first_name():
    return wait.until(EC.presence_of_element_located((By.NAME, "firstname")))


def last_name():
    return wait.until(EC.presence_of_element_located((By.NAME, "lastname")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def mobile():
    return wait.until(EC.presence_of_element_located((By.NAME, "telephone")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def confirm_password():
    return wait.until(EC.presence_of_element_located((By.NAME, "confirm")))

def agree():
    return wait.until(EC.presence_of_element_located((By.NAME, "agree")))

def btn_submit():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Continue']")))

def success_signup():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Congratulations! Your new account has been successfully created!')]")))

# def verify_otp_validation():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-verify-otp")))
#
# def your_otp_validation():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Your OTP is : ')]")))
#
# def verify():
#     return wait.until(EC.presence_of_element_located((By.NAME, "verify")))
#
# def my_profile():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'My Profile')]")))
#
# def delete_account_button():
#     return wait.until(EC.presence_of_element_located((By.ID, "btn-delete-account")))
#
# def yes_button():
#     return wait.until(EC.presence_of_element_located((By.ID, "btn-yes")))

def quit():
    return driver.quit()

class TestSignup:

    def test_validation(self):
        MyAccountPage().click()
        register().click()
        signup().click()
        assert first_name_validation().text == error.FIRST_NAME_VALIDATION
        assert last_name_validation().text == error.LAST_NAME_VALIDATION
        assert email_validation().text == error.EMAIL_VALIDATION
        assert mobile_no_validation().text == error.MOBILE_NO_VALIDATION
        assert set_password_validation().text == error.SET_PASSWORD_VALIDATION
        assert agree_validation().text == validation_assert.SELECT_AGREE

    def test_negative_cases(self):
        driver.refresh()
        first_name().send_keys(creds.INCORRECT_FIRSTNAME)
        last_name().send_keys(creds.INCORRECT_LASTNAME)
        email_input_field().send_keys(creds.INCORRECT_EMAIL)
        assert email_validation().text == error.EMAIL_VALIDATION
        mobile().send_keys(creds.INCORRECT_MOBILE)
        assert mobile_no_validation().text == error.MOBILE_NO_VALIDATION
        password_input_field().send_keys(creds.INCORRECT_PASSWORD)
        assert set_password_validation().text == error.SET_PASSWORD_VALIDATION
        confirm_password().send_keys(creds.INCORRECT_CONFIRM_PASSWORD)
        confirm_password().send_keys(Keys.BACKSPACE * 2)
        # assert confirm_password_validation().text == error.CONFIRM_PASSWORD_VALIDATION

        assert agree_validation().text == validation_assert.SELECT_AGREE
        signup().click()

    def test_email_validation(self):
        driver.refresh()
        signup_btn().click()
        first_name().send_keys(creds.FIRSTNAME)
        last_name().send_keys(creds.LASTNAME)
        email_input_field().send_keys(creds.EXISTING_EMAIL)
        mobile().send_keys(creds.MOBILE)
        password_input_field().send_keys(password)
        confirm_password().send_keys(password)
        agree().click()
        signup().click()
        time.sleep(1)
        assert exist_email_validation().text == validation_assert.EXIST_EMAIL

    def test_password_validation(self):
        driver.refresh()
        signup_btn().click()
        first_name().send_keys(creds.FIRSTNAME)
        last_name().send_keys(creds.LASTNAME)
        email_input_field().send_keys(creds.EMAIL_ID)
        mobile().send_keys(creds.MOBILE)
        password_input_field().send_keys(creds.INCORRECT_PASSWORD)
        confirm_password().send_keys(creds.INCORRECT_CONFIRM_PASSWORD)
        agree().click()
        btn_submit().click()
        time.sleep(1)
        assert confirm_password_validation().text == error.CONFIRM_PASSWORD_VALIDATION


    def test_positive_case(self):
        driver.refresh()
        signup_btn().click()
        first_name().send_keys(creds.FIRSTNAME)
        last_name().send_keys(creds.LASTNAME)
        self.email = random_string_generator() + '@gmail.com'
        print(self.email)
        email_input_field().send_keys(self.email)
        mobile().send_keys(creds.MOBILE)
        password_input_field().send_keys(password)
        confirm_password().send_keys(password)
        agree().click()
        # signup().click()
        btn_submit().click()
        # assert verify_otp_validation().text == error.VERIFY_OTP_VALIDATION
        # otp = your_otp_validation().text
        # verify().send_keys(otp)
        # verify().send_keys(Keys.ARROW_LEFT * 4 + Keys.SHIFT + Keys.ARROW_LEFT * 14 + Keys.DELETE)

        time.sleep(1)
        assert success_signup().text == validation_assert.SUCCESS_MESSAGE
        # delete_account_button().click()
        # yes_button().click()
        time.sleep(1)
        click_logout_button().click()
        driver.quit()
