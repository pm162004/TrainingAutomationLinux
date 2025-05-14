import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from OpenCart2.OpenCart_setup.config import config
from OpenCart2.Constant import validation_assert
from OpenCart2.Constant import input_field
import OpenCart2.Constant
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromeService

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# Only run with the latest Chrome version
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get(config.WEB_URL)
time.sleep(3)
wait = WebDriverWait(driver, 25)


def clickMyAccount():
    return driver.find_element(By.XPATH, "//span[normalize-space()='My Account']")

def clickLogin():
    return driver.find_element(By.LINK_TEXT,"Login")

def RefereshLogin():
    return driver.find_element(By.XPATH, "//a[@class='list-group-item'][normalize-space()='Login']")

def login_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']")))

def validation():
    email_pass = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")))
    return email_pass

def setEmail():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='input-email']")))

def setPassword():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='input-password']")))

# def pwd_validation():
#     pwd = wait.until(EC.presence_of_element_located((By.ID, "error-password")))
#     return pwd


def refresh_page():
    return driver.refresh()
#
#
# def mobile_no_input_field():
#     return wait.until(EC.presence_of_element_located((By.NAME, "mobile")))
#
#
# def password_input_field():
#     return wait.until(EC.presence_of_element_located((By.NAME, "password")))
#
#
def home_page_assert():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='My Account']")))
#
#
# def error_message():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-message")))
#
#
# def my_account_button():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='flex items-center ml-3']")))
#
#
def click_logout_button():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//aside[@id='column-right']//a[normalize-space()='Logout']")))


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
#

class TestLogin:
    def test_blank_field_validation(self):
        clickMyAccount().click()
        clickLogin().click()
        login_button().click()
        assert validation().text == validation_assert.ENTER_EMAIL_PASS


    def test_incorrect_email(self):
        refresh_page()
        RefereshLogin().click()
        setEmail().send_keys(input_field.INCORRECT_EMAIL)
        setPassword().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        assert validation().text == validation_assert.ENTER_EMAIL_PASS


    def test_incorrect_password(self):
        refresh_page()
        RefereshLogin().click()
        setEmail().send_keys(config.CORRECT_EMAIL)
        setPassword().send_keys(input_field.WRONG_PASSWORD[0])
        login_button().click()
        assert validation().text == validation_assert.ENTER_EMAIL_PASS


    def test_login(self):
        refresh_page()
        RefereshLogin().click()
        setEmail().send_keys(config.CORRECT_EMAIL)
        setPassword().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        time.sleep(2)
        assert home_page_assert().text == validation_assert.HOME_PAGE

    def test_logout(self):
        click_logout_button().click()
        refresh_page()
        RefereshLogin().click()
        driver.quit()


