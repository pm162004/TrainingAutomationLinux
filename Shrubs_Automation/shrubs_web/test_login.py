import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from Shrubs_Automation.shrubs_setup.config import config
from Shrubs_Automation.constant import validation_assert
from Shrubs_Automation.constant import input_field
from Shrubs_Automation.constant import error
import Shrubs_Automation.constant
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# Only run with the latest Chrome version
driver = webdriver.Chrome()
driver.maximize_window()
email = config.EMAIL
password = config.PASSWORD

# driver.set_window_size(1920, 1080)
driver.get(config.WEB_URL)
time.sleep(3)
wait = WebDriverWait(driver, 35)

def MyFilesPage():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def login_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-signin']")))


def email_blank_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required')]")))
    return email

def pass_blank_validation():
    passw = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Password is required')]")))
    return passw

def email_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is not valid.')]")))
    return email

def nonexist_email_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The selected email is invalid.')]")))
    return email

def password_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid credentials')]")))
    return email

def refresh_page():
    return driver.refresh()

def password_mask_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@d,'M12 7c2.76')]")))

class TestLogin:
    def test_blank_field_validation(self):
        login_button().click()
        assert email_blank_validation().text == validation_assert.ENTER_EMAIL
        assert pass_blank_validation().text == validation_assert.ENTER_PASSWORD

    def test_invalid_email(self):
        refresh_page()
        email_input_field().send_keys(input_field.INVALID_EMAIL)

        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        assert nonexist_email_validation().text == error.NON_EXIST_EMAIL

    def test_invalid_password(self):
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)

        password_input_field().send_keys(input_field.INVALID_PASSWORD)
        login_button().click()
        assert password_validation().text == error.PASS_VALIDATION

    def test_incorrect_email(self):
        refresh_page()
        email_input_field().send_keys(input_field.INCORRECT_EMAIL)

        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        assert email_validation().text == error.EMAIL_VALIDATION

    def test_incorrect_password(self):
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(input_field.INCORRECT_PASSWORD)
        login_button().click()
        assert password_validation().text == error.PASS_VALIDATION

    def test_both_invalid(self):
        refresh_page()
        email_input_field().send_keys(config.EMAIL)

        password_input_field().send_keys(config.PASSWORD)
        login_button().click()

    def test_valid(self):
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)

        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        assert MyFilesPage().text == validation_assert.MY_FILES



    # def test_login(self):
    #     click_login_button().click()
    #     refresh_page()
    #
    #     email_input_field().send_keys(config.CORRECT_EMAIL)
    #     password_input_field().send_keys(config.CORRECT_PASSWORD)
    #     login_button().click()
    #     time.sleep(2)
    #     assert home_page_assert().text == validation_assert.HOME_PAGE
    #
    # def test_logout(self):
    #     # MyAccountPage().click()
    #     click_logout_button().click()
    #     driver.quit()
    #     # assert assert_login_page_mobile().text == validation_assert.LOGIN_GET_VALIDATE[0]
    #     # assert assert_login_page_pwd().text == validation_assert.LOGIN_GET_VALIDATE[1]

    # def test_unverified_user(self):
    #     email_input_field().send_keys(input_field.UNVERIFIED_USER_EMAIL)
    #     password_input_field().send_keys(config.CORRECT_PASSWORD)
    #     login_button().click()
    #     assert assert_verify_with_otp().text == validation_assert.VERIFY_WITH_OTP
    #     driver.quit()

    # def test_invalid_phone_no(self):
    #     refresh_page()
    #     mobile_no_input_field().send_keys(input_field.INVALID_PHONE_NO[0])
    #     assert mobile_no_validation().text == validation_assert.INVALID_PHONE_NO_ASSERT
    #     password_input_field().send_keys(config.CORRECT_PASSWORD)
    #     login_button().click()
    #
    # def test_incorrect_pwd_length(self):
    #     refresh_page()
    #     mobile_no_input_field().send_keys(config.CORRECT_MOBILE)
    #     password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
    #     assert pwd_validation().text == validation_assert.PWD_LENGTH
    #     login_button().click()



    # def test_wrong_password(self):
    #     refresh_page()
    #     mobile_no_input_field().send_keys(config.CORRECT_MOBILE)
    #     password_input_field().send_keys(input_field.WRONG_PASSWORD[2])
    #     login_button().click()
    #     assert error_message().text == validation_assert.INVALID_CREDS


