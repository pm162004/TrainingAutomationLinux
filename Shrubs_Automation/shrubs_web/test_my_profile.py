import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Shrubs_Automation.shrubs_setup.config import config
from Shrubs_Automation.constant import creds, validation_assert, input_field, error

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# Only run with the latest Chrome version
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get(config.WEB_URL)
email = config.CORRECT_EMAIL
password = config.PASSWORD
wait = WebDriverWait(driver, 25)

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))


def login_password():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def refresh_page():
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait for the body to load after refresh


def MyFilesPage():
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def droppable_area():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//i[normalize-space()='arrow_drop_down']")))
#
# def login_button():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='header-login-btn cursor-pointer ml-6']")))
#
#
# def register_button():
#     return wait.until(EC.element_to_be_clickable((By.ID, "btn-register")))
#
#
# def first_name():
#     return wait.until(EC.presence_of_element_located((By.ID, "first-name")))
#
#
# def last_name():
#     return wait.until(EC.presence_of_element_located((By.ID, "last-name")))
#
#
# def mobile_no():
#     return wait.until(EC.presence_of_element_located((By.ID, "mobile")))
#
#
# def password_validation():
#     return wait.until(EC.presence_of_element_located((By.ID, "password")))
#
#
# def confirm_password():
#     return wait.until(EC.presence_of_element_located((By.ID, "confirm-password")))
#
#
# def sign_up():
#     return wait.until(EC.presence_of_element_located((By.ID, "btn-signup")))
#
#
# def submit():
#     return wait.until(EC.presence_of_element_located((By.ID, "btn-submit")))
#
#
# def error_verify_otp():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-verify-otp")))
#
#
# def your_otp_validation():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Your OTP is : ')]")))
#
#
# def verify():
#     return wait.until(EC.presence_of_element_located((By.NAME, "verify")))
#
#
# def submit_button():
#     return wait.until(EC.presence_of_element_located((By.ID, "btn-submit")))
#
#
# def my_profile():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'My Profile')]")))
#
#
# def btn_save_profile():
#     return wait.until(EC.element_to_be_clickable((By.ID, "btn-save-profile")))
#
#
# def email_validation():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-email")))
#
#
# def date_validation():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-birth-date")))
#
#
# def gender_validation():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-gender")))
#
#
# def state_validation():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-state")))
#
#
# def city_validation():
#     return wait.until(EC.presence_of_element_located((By.ID, "error-city")))
#
#
# def email_valid():
#     return wait.until(EC.presence_of_element_located((By.ID, "email")))
#
#
# def datepicker_icon():
#     return wait.until(EC.element_to_be_clickable((By.ID, "datepicker-icon")))
#
#
# def month_selection():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='August 2023']")))
#
#
# def select_arrow():
#     return wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//button[@class='v3dp__heading__center'][normalize-space()='2023']")))
#
#
# def heading_select():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='v3dp__heading__button'][1]")))
#
#
# def year_select():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'2000')]")))
#
#
# def month_select():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'May')]")))
#
#
# def date_select():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'17')]")))
#
#
# def select_box():
#     return wait.until(EC.element_to_be_clickable((By.ID, "vs6__combobox")))
#
#
# def select_option():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id='vs6__option-0']")))
#
#
# def select_dropdown():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='vs8__combobox']")))
#
#
# def select_dropdown_option():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id='vs8__option-11']")))
#
#
# def select_city_dropdown():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='vs9__combobox']")))
#
#
# def select_city_option():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id='vs9__option-4']")))
#
#
# def email_pop_message():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Please verify your email ID')]")))
#
#
# def btn_pop_close():
#     return wait.until(EC.element_to_be_clickable((By.ID, "btn-popup-close")))
#
#
# def btn_email_verify():
#     return wait.until(EC.element_to_be_clickable((By.ID, "btn-email-verify")))
#
#
# def btn_verify_otp():
#     return wait.until(EC.element_to_be_clickable((By.ID, "btn-verify-otp")))
#
#
# def verify_otp():
#     return wait.until(EC.presence_of_element_located((By.ID, "verify-otp")))
#
#
# def email_exist_message():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Email ID already Exists')]")))
#
#
# def grow_your_money():
#     return wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Grow your Money')]")))
#
#
# def assert_my_profile():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex items-center ml-3']//*[name()='svg']")))
#
#
# def my_profile_validation():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'My Profile')]")))
#
#
# def clear():
#     return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='vs__clear']")))
#
#
# def select_gender():
#     return wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//div[@class='vs__selected-options']//input[@placeholder='Select']")))
#
#
# def delete_account_btn():
#     return wait.until(EC.presence_of_element_located((By.ID, "btn-delete-account")))
#
#
# def button_yes():
#     return wait.until(EC.presence_of_element_located((By.ID, "btn-yes")))
#
#
# def delete_message():
#     return wait.until(
#         EC.presence_of_element_located((By.XPATH, "//p[@class='text-base text-dark font-bold px-8 mt-3 md:mt-6']")))
#
#
# def quit():
#     return driver.quit()
#

class TestMyProfile:


  def test_login(self):
     email_input_field().send_keys(email)
     login_password().send_keys(password)
     btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
     btn_login.click()
     time.sleep(5)
     assert MyFilesPage().text == validation_assert.MY_FILES

  def test_my_profile(self):
      droppable_area().click()
#
#
# def test_my_profile_validation(self):
#     login_button().click()
#     register_button().click()
#     first_name().send_keys(creds.FIRSTNAME)
#     last_name().send_keys(creds.LASTNAME)
#     mobile_no().send_keys(creds.MY_PROFILE_PHONE)
#     password_validation().send_keys(password)
#     confirm_password().send_keys(password)
#     sign_up().click()
#     submit().click()
#     time.sleep(1)
#     assert error_verify_otp().text == error.VERIFY_OTP_VALIDATION
#     otp = your_otp_validation().text
#     verify().send_keys(otp)
#     verify().send_keys(Keys.ARROW_LEFT * 4 + Keys.SHIFT + Keys.ARROW_LEFT * 14 + Keys.DELETE)
#     submit_button().click()
#     assert my_profile().text == error.MY_PROFILE_VALIDATION
#     btn_save_profile().click()
#     assert email_validation().text == error.EMAIL_VALIDATION
#     assert date_validation().text == error.DATE_VALIDATION
#     assert gender_validation().text == error.GENDER_VALIDATION
#     assert state_validation().text == error.STATE_VALIDATION
#     assert city_validation().text == error.CITY_VALIDATION
#
#
# def test_data_validation(self):
#     email_valid().send_keys(creds.EMAIL_ID)
#     datepicker_icon().click()
#     month_selection().click()
#     select_arrow().click()
#     heading_select().click()
#     heading_select().click()
#     year_select().click()
#     month_select().click()
#     date_select().click()
#     select_box().click()
#     select_option().click()
#     select_dropdown().click()
#     select_dropdown_option().click()
#     select_city_dropdown().click()
#     select_city_option().click()
#     btn_save_profile().click()
#     assert email_pop_message().text == error.EMAIL_POP_MESSAGE
#     btn_pop_close().click()
#     time.sleep(1)
#
#
# def test_otp_validation(self):
#     btn_email_verify().click()
#     btn_verify_otp().click()
#     otp = error_verify_otp().text
#     assert otp == error.OTP_VALIDATION
#     otp = your_otp_validation().text
#     verify_otp().send_keys(otp)
#     verify_otp().send_keys(Keys.ARROW_LEFT * 4 + Keys.SHIFT + Keys.ARROW_LEFT * 14 + Keys.DELETE)
#     btn_verify_otp().click()
#     time.sleep(1)
#
#
# def test_email_validation(self):
#     email_valid().send_keys(Keys.CONTROL + 'A' + Keys.BACKSPACE)
#     email_valid().send_keys(creds.VERIFIED_EMAIL)
#     btn_save_profile().click()
#     assert email_exist_message().text == error.EXIST_EMAIL_MESSAGE
#     btn_pop_close().click()
#
#
# def test_validation(self):
#     email_valid().send_keys(Keys.CONTROL + 'A' + Keys.BACKSPACE)
#     email_valid().send_keys(creds.EMAIL_ID)
#     btn_save_profile().click()
#
#
# def test_updates(self):
#     assert grow_your_money().text == error.HOME_MESSAGE
#     assert_my_profile().click()
#     my_profile_validation().click()
#     clear().click()
#     select_gender().click()
#     select_gender().send_keys(Keys.ARROW_DOWN * 2 + Keys.ENTER)
#     delete_account_btn().click()
#     button_yes().click()
#     assert delete_message().text == error.DELETE_MESSAGE
#     time.sleep(2)
#     driver.quit()
