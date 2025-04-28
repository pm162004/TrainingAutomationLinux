import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from Opencart2.opencart_setup.config import config
from Opencart2.constant import validation_assert
from Opencart2.constant import input_field
import Opencart2.constant
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
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']")))


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
    return wait.until(EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='My Account']")))


# def error_message():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-message")))
#
#
# def my_account_button():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='flex items-center ml-3']")))


def click_logout_button():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//aside[@id='column-right']//a[normalize-space()='Logout']")))

def click_login_button():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//aside[@id='column-right']//a[normalize-space()='Login']")))


# def assert_login_page_mobile():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='mobile-no']")))
#
#
# def assert_login_page_pwd():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Enter Password']")))
#
#
# def assert_verify_with_otp():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Enter OTP']")))


class TestLogin:
    def test_blank_field_validation(self):
        MyAccountPage().click()
        login_page().click()
        login_button().click()
        assert email_pass_validation().text == validation_assert.EMAIL_PASS_VALIDATION


    def test_incorrect_email(self):
        refresh_page()
        click_login_button().click()
        email_input_field().send_keys(input_field.INVALID_EMAIL_ID_INPUT)

        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        assert email_pass_validation().text == validation_assert.EMAIL_PASS_VALIDATION

    def test_incorrect_password(self):
        refresh_page()
        click_login_button().click()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(input_field.WRONG_PASSWORD[0])
        login_button().click()
        assert email_pass_validation().text == validation_assert.EMAIL_PASS_VALIDATION

    def test_login(self):
        click_login_button().click()
        refresh_page()

        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        time.sleep(2)
        assert home_page_assert().text == validation_assert.HOME_PAGE

    def test_logout(self):
        # MyAccountPage().click()
        click_logout_button().click()
        driver.quit()
        # assert assert_login_page_mobile().text == validation_assert.LOGIN_GET_VALIDATE[0]
        # assert assert_login_page_pwd().text == validation_assert.LOGIN_GET_VALIDATE[1]

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


