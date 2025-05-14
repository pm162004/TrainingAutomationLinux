import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from OpenCart2.OpenCart_setup.config import config
from OpenCart2.Constant import validation_assert
from OpenCart2.Constant import input_field
import OpenCart2.Constant
from OpenCart2.Constant import creds
from OpenCart2.Constant import error

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# Only run with the latest Chrome version
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get(config.WEB_URL)
email = config.CORRECT_EMAIL
password = config.PASSWORD
wait = WebDriverWait(driver, 25)

def login_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']")))

def register():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "a[class='btn btn-primary']")))

def clickMyAccount():
    return driver.find_element(By.XPATH, "//span[normalize-space()='My Account']")

def clickRegister():
    return driver.find_element(By.LINK_TEXT,"Register")
# def signup():
#     return wait.until(EC.element_to_be_clickable((By.ID, "btn-signup")))

def first_name_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'First Name must be between 1 and 32 characters!')]")))

def last_name_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]")))

def email_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'E-Mail Address does not appear to be valid!')]")))

def exist_email_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")))

def mobile_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]")))

def set_password_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Password must be between 4 and 20 characters!')]")))

def confirm_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Password confirmation does not match password!')]")))

def agree_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")))

# def confirm_password_validation():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-confirm-password")))

def first_name():
    return wait.until(EC.presence_of_element_located((By.NAME, "firstname")))

def last_name():
    return wait.until(EC.presence_of_element_located((By.NAME, "lastname")))

def email():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def phone_no():
    return wait.until(EC.presence_of_element_located((By.NAME, "telephone")))

# def first_name_negative_validation():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-first-name")))


def password():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def confirm_password():
    return wait.until(EC.presence_of_element_located((By.NAME, "confirm")))

def check_agree():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='agree']")))



def btn_submit():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Continue']")))


def my_success():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Congratulations! Your new account has been successfully created!')]")))
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

        clickMyAccount().click()
        clickRegister().click()
        # login_button().click()
        btn_submit().click()
        assert first_name_validation().text == error.FIRST_NAME_VALIDATION
        assert last_name_validation().text == error.LAST_NAME_VALIDATION
        assert email_validation().text == error.EMAIL_VALIDATION
        assert mobile_validation().text == error.PHONE_NO_VALIDATION
        assert set_password_validation().text == error.SET_PASSWORD_VALIDATION
        assert agree_validation().text == validation_assert.SELECT_AGREE

    def test_negative_cases(self):
        driver.refresh()
        first_name().send_keys(creds.INCORRECT_FIRSTNAME)
        last_name().send_keys(creds.INCORRECT_FIRSTNAME)
        email().send_keys(creds.INCORRECT_EMAIL)
        assert email_validation().text == error.EMAIL_VALIDATION
        phone_no().send_keys(creds.INCORRECT_MOBILE)
        assert mobile_validation().text == error.PHONE_NO_VALIDATION
        password().send_keys(creds.INCORRECT_PASSWORD)

        confirm_password().send_keys(creds.INCORRECT_CONFIRM_PASSWORD)
        # assert confirm_validation().text == error.CONFIRM_PASSWORD_VALIDATION
        btn_submit().click()
        check_agree().click()
        assert agree_validation().text == validation_assert.SELECT_AGREE
        btn_submit().click()

 #
    def test_password_validation(self):
        driver.refresh()
        first_name().send_keys(creds.FIRSTNAME)
        last_name().send_keys(creds.LASTNAME)
        email().send_keys(creds.EXISTING_EMAIL)
        phone_no().send_keys(creds.PHONE)
        password().send_keys(creds.PASSWORD)
        confirm_password().send_keys(creds.PASSWORD)
        check_agree().click()
        btn_submit().click()
        time.sleep(1)
        assert exist_email_validation().text == validation_assert.ENTER_EXIST_EMAIL

    def test_email_validation(self):
        driver.refresh()
        first_name().send_keys(creds.FIRSTNAME)
        last_name().send_keys(creds.LASTNAME)
        email().send_keys(creds.EXISTING_EMAIL)
        phone_no().send_keys(creds.PHONE)
        password().send_keys(creds.PASSWORD)
        confirm_password().send_keys(creds.PASSWORD)
        check_agree().click()
        btn_submit().click()
        time.sleep(1)
        assert exist_email_validation().text == validation_assert.ENTER_EXIST_EMAIL

    # def test_positive_case(self):
    #     driver.refresh()
    #     first_name().send_keys(creds.FIRSTNAME)
    #     last_name().send_keys(creds.LASTNAME)
    #     mobile_validation().send_keys(mobile)
    #     valid_password().send_keys(password)
    #     confirm_password().send_keys(password)
    #     signup().click()
    #     btn_submit().click()
    #     assert verify_otp_validation().text == error.VERIFY_OTP_VALIDATION
    #     otp = your_otp_validation().text
    #     verify().send_keys(otp)
    #     verify().send_keys(Keys.ARROW_LEFT * 4 + Keys.SHIFT + Keys.ARROW_LEFT * 14 + Keys.DELETE)
    #     btn_submit().click()
    #     time.sleep(1)
    #     assert my_profile().text == error.MY_PROFILE_VALIDATION
    #     delete_account_button().click()
    #     yes_button().click()
    #     time.sleep(1)
    #     driver.quit()
