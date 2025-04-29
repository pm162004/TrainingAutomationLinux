import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from Opencart2.opencart_setup.config import config
from Opencart2.constant import validation_assert, creds
from Opencart2.constant import error
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
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Your Store']")))

def add_cart():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='content']//div[1]//div[1]//div[3]//button[1]")))

def your_store():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Your Store']")))


def email_pass_validation():
    email_pass = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")))
    return email_pass

def click_cart():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")))

def checkout():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//body//header//div[@id='cart']//div//a[1]")))

# def pwd_validation():
#     pwd = wait.until(EC.presence_of_element_located((By.ID, "error-password")))
#     return pwd
def first_name_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'First Name must be between 1 and 32 characters!')]")))

def last_name_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]")))

def address_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Address 1 must be between 3 and 128 characters!')]")))

def city_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'City must be between 2 and 128 characters!')]")))

def postcode_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Postcode must be between 2 and 10 characters!')]")))

def country_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='input-payment-country']")))

def region_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Postcode must be between 2 and 10 characters!')]")))

def continue_bill():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='button-payment-address']")))

def agree_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")))


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
def first_name():
    return wait.until(EC.presence_of_element_located((By.NAME, "firstname")))


def last_name():
    return wait.until(EC.presence_of_element_located((By.NAME, "lastname")))

def address1():
    return wait.until(EC.presence_of_element_located((By.NAME, "address_1")))

def address2():
    return wait.until(EC.presence_of_element_located((By.NAME, "address_2")))

def company():
    return wait.until(EC.presence_of_element_located((By.NAME, "company")))

def city():
    return wait.until(EC.presence_of_element_located((By.NAME, "city")))

def postcode():
    return wait.until(EC.presence_of_element_located((By.NAME, "postcode")))

def country():
    drop = driver.find_element(By.NAME, "country_id")


    return wait.until(EC.element_to_be_clickable((By.XPATH, "//option[normalize-space()='India']")))


def region():
    drop = driver.find_element(By.NAME, "zone_id")
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//option[normalize-space()='Gujarat']")))
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
    # def test_blank_field_validation(self):
    #     MyAccountPage().click()
    #     MyAccountPage().click()
    #     if MyAccountPage().text == "Logout":
    #         click_logout_button()
    #     login_page().click()
    #     login_button().click()
    #     assert email_pass_validation().text == validation_assert.EMAIL_PASS_VALIDATION
    #
    #
    # def test_incorrect_email(self):
    #     refresh_page()
    #     click_login_button().click()
    #     email_input_field().send_keys(input_field.INVALID_EMAIL_ID_INPUT)
    #
    #     password_input_field().send_keys(config.CORRECT_PASSWORD)
    #     login_button().click()
    #     assert email_pass_validation().text == validation_assert.EMAIL_PASS_VALIDATION
    #
    # def test_incorrect_password(self):
    #     refresh_page()
    #     click_login_button().click()
    #     email_input_field().send_keys(config.CORRECT_EMAIL)
    #     password_input_field().send_keys(input_field.WRONG_PASSWORD[0])
    #     login_button().click()
    #     assert email_pass_validation().text == validation_assert.EMAIL_PASS_VALIDATION

    def test_login(self):
        MyAccountPage().click()
        login_page().click()
        # click_login_button().click()


        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        time.sleep(2)
        assert your_store().text == validation_assert.YOUR_STORE
        # driver.quit()

    def test_order_blank(self):
        add_cart().click()
        click_cart().click()
        checkout().click()
        login_page().click()
        # click_login_button().click()

        continue_bill().click()

        assert first_name_validation().text == error.FIRST_NAME_VALIDATION
        assert last_name_validation().text == error.LAST_NAME_VALIDATION
        assert address_validation().text == error.ADDRESS_VALIDATION
        assert city_validation().text == error.CITY_VALIDATION
        assert postcode_validation().text == error.POSTCODE_VALIDATION
        assert country_validation().text == error.COUNTRY_VALIDATION
        assert region_validation().text == error.REGION_VALIDATION


    def test_order(self):
        # add_cart().click()
        # click_cart().click()
        # checkout().click()
        # login_page().click()
        # # click_login_button().click()
        #
        # continue_bill().click()
        first_name().send_keys(creds.FIRSTNAME)
        last_name().send_keys(creds.LASTNAME)
        company().send_keys(creds.COMPANY_NAME)
        address1().send_keys(creds.ADDRESS1)
        address2().send_keys(creds.ADDRESS2)
        city().send_keys(creds.CITY)
        postcode().send_keys(creds.POSTAL_CODE)
        country().click()
        region().click()
        # assert first_name_validation().text == error.FIRST_NAME_VALIDATION
        # assert last_name_validation().text == error.LAST_NAME_VALIDATION
        # assert address_validation().text == error.ADDRESS_VALIDATION
        # assert city_validation().text == error.CITY_VALIDATION
        # assert postcode_validation().text == error.POSTCODE_VALIDATION
        # assert country_validation().text == error.COUNTRY_VALIDATION
        # assert region_validation().text == error.REGION_VALIDATION
        driver.quit()
    # def test_logout(self):
    #     # MyAccountPage().click()
    #     click_logout_button().click()
    #     driver.quit()
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


