import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from OpenCart2.opencart_setup.config import config
from OpenCart2.constant import validation_assert
from OpenCart2.constant import input_field
import OpenCart2.constant
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# Only run with the latest Chrome version
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get(config.WEB_URL)
time.sleep(3)
wait = WebDriverWait(driver, 25)

def MyAccountPage():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='My Account']")))

def login_page():
    return wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))


def login_button():
    return wait.until(EC.element_to_be_clickable((By.ID, "btn-login")))


def email_pass_validation():
    email_pass = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")))
    return email_pass

#
# def pwd_validation():
#     pwd = wait.until(EC.presence_of_element_located((By.ID, "error-password")))
#     return pwd


def refresh_page():
    return driver.refresh()


def email_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='input-email']")))


def password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='input-password']")))


def home_page_assert():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Grow your Money')]")))


def error_message():
    return wait.until(EC.presence_of_element_located((By.ID, "error-message")))


def my_account_button():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='flex items-center ml-3']")))


def click_logout_button():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Logout']")))


def assert_login_page_mobile():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='mobile-no']")))


def assert_login_page_pwd():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Enter Password']")))


def assert_verify_with_otp():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Enter OTP']")))


class TestLogin:
    def test_blank_field_validation(self):
        login_page().click()
        login_button().click()
        assert mobile_no_validation().text == validation_assert.ENTER_MOBILE_NO
        assert pwd_validation().text == validation_assert.ENTER_PASSWORD

    def test_incorrect_phone_no(self):
        refresh_page()
        mobile_no_input_field().send_keys(input_field.INCORRECT_MOBILE_NO)
        assert mobile_no_validation().text == validation_assert.INCORRECT_MOBILE_NO_VALIDATION
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()

    def test_invalid_phone_no(self):
        refresh_page()
        mobile_no_input_field().send_keys(input_field.INVALID_PHONE_NO[0])
        assert mobile_no_validation().text == validation_assert.INVALID_PHONE_NO_ASSERT
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()

    def test_incorrect_pwd_length(self):
        refresh_page()
        mobile_no_input_field().send_keys(config.CORRECT_MOBILE)
        password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
        assert pwd_validation().text == validation_assert.PWD_LENGTH
        login_button().click()

    def test_invalid_password(self):
        refresh_page()
        mobile_no_input_field().send_keys(config.CORRECT_MOBILE)
        password_input_field().send_keys(input_field.WRONG_PASSWORD[0])
        assert pwd_validation().text == validation_assert.INVALID_PWD
        login_button().click()

    def test_wrong_password(self):
        refresh_page()
        mobile_no_input_field().send_keys(config.CORRECT_MOBILE)
        password_input_field().send_keys(input_field.WRONG_PASSWORD[2])
        login_button().click()
        assert error_message().text == validation_assert.INVALID_CREDS

    def test_login(self):
        refresh_page()
        mobile_no_input_field().send_keys(config.CORRECT_MOBILE)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        time.sleep(2)
        assert home_page_assert().text == validation_assert.HOME_PAGE

    def test_logout(self):
        my_account_button().click()
        click_logout_button().click()
        assert assert_login_page_mobile().text == validation_assert.LOGIN_GET_VALIDATE[0]
        assert assert_login_page_pwd().text == validation_assert.LOGIN_GET_VALIDATE[1]

    def test_unverified_user(self):
        mobile_no_input_field().send_keys(input_field.UNVERIFIED_USER_NUMBER)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        assert assert_verify_with_otp().text == validation_assert.VERIFY_WITH_OTP
        driver.quit()
