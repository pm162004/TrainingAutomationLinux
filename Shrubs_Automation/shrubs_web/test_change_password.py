import time

from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Shrubs_Automation.shrubs_setup.config import config
from Shrubs_Automation.constant import creds,validation_assert,input_field
from Shrubs_Automation.constant import error
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# Only run with the latest Chrome version
driver = webdriver.Chrome()
# driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.get(config.WEB_URL)
email = config.CORRECT_EMAIL
password = config.PASSWORD
new_password = config.RESET_PASSWORD
wait = WebDriverWait(driver, 25)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))


def forgot_password_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='custom-link']")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def email_blank_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required')]")))
    return email

def email_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is not valid.')]")))
    return email

def nonexist_email_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The selected email is invalid.')]")))
    return email

def resend_link_button():
    btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    return btn

def open_new_tab():

    # return driver.execute_script("window.open('https://www.mailinator.com/');")
    return driver.get("https://www.mailinator.com/")


def yopmail_email_input_field():

        # Wait for the email input field to be clickable inside the iframe
       return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))


def select_mail():
    # Wait for the email input field to be clickable inside the iframe
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(text(),'🛠️ Did You Lose Your Password… Again?')]")))

def select_reset_btn():
    # Switch to the iframe with the specified id
    driver.switch_to.frame("html_msg_body")

    # Wait until the reset button is present and clickable
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'🔗 Reset My Password')]")))

def select_reset_btn():
        # Switch to the iframe with the specified id
    driver.switch_to.frame("html_msg_body")

    # Wait until the reset button is present and clickable
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'🔗 Reset My Password')]")))

def reset_password_link():
    return wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
    # return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your inbox here']")))
def valid_password():
    return wait.until(EC.presence_of_element_located((By.NAME, "new-password")))

def valid_confirm_password():
    return wait.until(EC.presence_of_element_located((By.NAME, "confirm-password")))
#
# def btn_login():
#     return wait.until(EC.presence_of_element_located((By.ID, "btn-login")))
#
# def forget_password():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex items-center ml-3']//*[name()='svg']")))
#
# def change_password():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Change Password')]")))
#
# def btn_change_password():
#     return wait.until(EC.element_to_be_clickable((By.ID, "btn-change-password")))
#
# def current_password_validation():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-password")))
#
def new_password_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'New Password is required')]")))

def confirm_password_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Repeat New Password is required')]")))
#
# def valid_new_password():
#     return wait.until(EC.presence_of_element_located((By.ID, "new-password")))
#
# def invalid_confirm_password():
#     return wait.until(EC.presence_of_element_located((By.ID, "confirm-password")))
#
# def error_confirm_password():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-confirm-password")))
#
# def same_password():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-msg")))
#
# def hide_password():
#     return wait.until(EC.element_to_be_clickable((By.ID, "hide-password")))
#
# def success_message():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Your password has been changed')]")))
#
# def close_popup():
#     return wait.until(EC.element_to_be_clickable((By.ID, "close-popup")))
#
# def logout_validation():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Logout')]")))
#
def refresh_page():
    return driver.refresh()

class TestChangePassword:

    # def test_login_case(self):
    #  forgot_password_button().click()

    def test_blank_field_validation(self):
     forgot_password_button().click()
     time.sleep(3)
     resend_link_button().click()

     assert email_blank_validation().text == validation_assert.ENTER_EMAIL
     time.sleep(3)


    def test_invalid_email(self):
      refresh_page()
      email_input_field().send_keys(input_field.INCORRECT_PASSWORD)
      resend_link_button().click()
      assert email_validation().text == error.EMAIL_VALIDATION

    def test_nonexist_email(self):
        refresh_page()

        email_input_field().send_keys(creds.EXISTING_EMAIL)
        resend_link_button().click()
        assert nonexist_email_validation().text == error.NON_EXIST_EMAIL

    def test_valid_email(self):
        refresh_page()

        email_input_field().send_keys(email)
        resend_link_button().click()
        open_new_tab()

    def test_resend_link(self):
        time.sleep(3)
        yopmail_email_input_field().send_keys(email)
        yopmail_email_input_field().send_keys(Keys.ENTER)
        time.sleep(3)
        select_mail().click()
        time.sleep(3)
        select_reset_btn().click()

    def test_password_validation(self):
        reset_password_link().click()

        assert new_password_validation().text == validation_assert.ENTER_NEW_PASSWORD
        assert confirm_password_validation().text == validation_assert.ENTER_CONFIRM_PASSWORD
    #
    # def test_confirm_validation(self):
    #     valid_password().send_keys(password)
    #     valid_new_password().send_keys(new_password)
    #     invalid_confirm_password().send_keys(password)
    #     assert error_confirm_password().text == error.CONFIRM_PASSWORD_ERROR
    #
    # def test_current_validation(self):
    #     valid_password().send_keys(Keys.BACKSPACE * 3)
    #     assert current_password_validation().text == error.CURRENT_PASSWORD_ERROR
    #
    # def test_new_password_validation(self):
    #     driver.refresh()
    #     valid_password().send_keys(password)
    #     valid_new_password().send_keys(password)
    #     invalid_confirm_password().send_keys(password)
    #     btn_change_password().click()
    #     assert same_password().text == error.SAME_PASSWORD_ERROR
    #
    # def test_old_password_validation(self):
    #     driver.refresh()
    #     valid_password().send_keys(new_password)
    #     valid_new_password().send_keys(password)
    #     invalid_confirm_password().send_keys(password)
    #     btn_change_password().click()
    #     assert same_password().text == error.OLD_PASSWORD_ERROR
    #
    # def test_copy_password(self):
    #     driver.refresh()
    #     valid_password().send_keys(password)
    #     hide_password().click()
    #     valid_password().send_keys(Keys.CONTROL + 'A' + Keys.CONTROL + 'C')
    #     valid_new_password().send_keys(Keys.CONTROL + 'v')
    #
    # def test_positive_validation(self):
    #     driver.refresh()
    #     valid_password().send_keys(password)
    #     valid_new_password().send_keys(new_password)
    #     invalid_confirm_password().send_keys(new_password)
    #     btn_change_password().click()
    #     assert success_message().text == error.PASSWORD_SUCCESS_MESSAGE
    #     close_popup().click()
    #
    # def test_sign_out_login_case(self):
    #     forget_password().click()
    #     logout_validation().click()
    #     valid_mobile().send_keys(creds.CHANGE_MOBILE)
    #     valid_password().send_keys(new_password)
    #     btn_login().click()
    #     forget_password().click()
    #     change_password().click()
    #     valid_password().send_keys(new_password)
    #     valid_new_password().send_keys(password)
    #     invalid_confirm_password().send_keys(password)
    #     btn_change_password().click()
    #     close_popup().click()
    #     driver.quit()
