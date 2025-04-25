import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from valor_setup.config import config
import constant
from constant import creds
from constant import error
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# Only run with the latest Chrome version
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()),
    options=chrome_options
)
driver.set_window_size(1920, 1080)
driver.get(config.WEB_URL)
mobile = config.MOBILE
password = config.PASSWORD
wait = WebDriverWait(driver, 25)

def login_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='header-login-btn cursor-pointer ml-6']")))

def register():
    return wait.until(EC.element_to_be_clickable((By.ID, "btn-register")))

def signup():
    return wait.until(EC.element_to_be_clickable((By.ID, "btn-signup")))

def first_name_validation():
    return wait.until(EC.presence_of_element_located((By.ID, "error-first-name")))

def last_name_validation():
    return wait.until(EC.presence_of_element_located((By.ID, "error-last-name")))

def mobile_no_validation():
    return wait.until(EC.presence_of_element_located((By.ID, "error-mobile")))

def set_password_validation():
    return wait.until(EC.presence_of_element_located((By.ID, "error-password")))

def confirm_password_validation():
    return wait.until(EC.presence_of_element_located((By.ID, "error-confirm-password")))

def first_name():
    return wait.until(EC.presence_of_element_located((By.ID, "first-name")))

def first_name_negative_validation():
    return wait.until(EC.presence_of_element_located((By.ID, "error-first-name")))

def mobile_validation():
    return wait.until(EC.presence_of_element_located((By.ID, "mobile")))

def valid_password():
    return wait.until(EC.presence_of_element_located((By.ID, "password")))

def confirm_password():
    return wait.until(EC.presence_of_element_located((By.ID, "confirm-password")))

def last_name():
    return wait.until(EC.presence_of_element_located((By.ID, "last-name")))

def phone_no_validation():
    return wait.until(EC.presence_of_element_located((By.ID, "error-message")))

def btn_submit():
    return wait.until(EC.presence_of_element_located((By.ID, "btn-submit")))

def verify_otp_validation():
    return wait.until(EC.presence_of_element_located((By.ID, "error-verify-otp")))

def your_otp_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Your OTP is : ')]")))

def verify():
    return wait.until(EC.presence_of_element_located((By.NAME, "verify")))

def my_profile():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'My Profile')]")))

def delete_account_button():
    return wait.until(EC.presence_of_element_located((By.ID, "btn-delete-account")))

def yes_button():
    return wait.until(EC.presence_of_element_located((By.ID, "btn-yes")))

def quit():
    return driver.quit()

class TestSignup:

    def test_validation(self):
        login_button().click()
        register().click()
        signup().click()
        assert first_name_validation().text == error.FIRST_NAME_VALIDATION
        assert last_name_validation().text == error.LAST_NAME_VALIDATION
        assert mobile_no_validation().text == error.MOBILE_NO_VALIDATION
        assert set_password_validation().text == error.SET_PASSWORD_VALIDATION
        assert confirm_password_validation().text == error.CONFIRM_PASSWORD_VALIDATION

    def test_negative_cases(self):
        driver.refresh()
        first_name().send_keys(creds.INCORRECT_FIRSTNAME)
        assert first_name_negative_validation().text == error.FIRST_NAME_NEGATIVE_VALIDATION
        mobile_validation().send_keys(creds.INCORRECT_MOBILE)
        assert mobile_no_validation().text == error.MOBILE_NO_NEGATIVE_VALIDATION
        valid_password().send_keys(creds.INCORRECT_PASSWORD)
        assert set_password_validation().text == error.SET_PASSWORD_NEGATIVE_VALIDATION
        confirm_password().send_keys(creds.INCORRECT_CONFIRM_PASSWORD)
        confirm_password().send_keys(Keys.BACKSPACE * 2)
        assert confirm_password_validation().text == error.CONFIRM_PASSWORD_NEGATIVE_VALIDATION

    def test_phone_no_validation(self):
        driver.refresh()
        first_name().send_keys(creds.FIRSTNAME)
        last_name().send_keys(creds.LASTNAME)
        mobile_validation().send_keys(creds.EXISTING_MOBILE_NO)
        valid_password().send_keys(password)
        confirm_password().send_keys(password)
        signup().click()
        time.sleep(1)
        assert phone_no_validation().text == error.PHONE_NO_VALIDATION

    def test_positive_case(self):
        driver.refresh()
        first_name().send_keys(creds.FIRSTNAME)
        last_name().send_keys(creds.LASTNAME)
        mobile_validation().send_keys(mobile)
        valid_password().send_keys(password)
        confirm_password().send_keys(password)
        signup().click()
        btn_submit().click()
        assert verify_otp_validation().text == error.VERIFY_OTP_VALIDATION
        otp = your_otp_validation().text
        verify().send_keys(otp)
        verify().send_keys(Keys.ARROW_LEFT * 4 + Keys.SHIFT + Keys.ARROW_LEFT * 14 + Keys.DELETE)
        btn_submit().click()
        time.sleep(1)
        assert my_profile().text == error.MY_PROFILE_VALIDATION
        delete_account_button().click()
        yes_button().click()
        time.sleep(1)
        driver.quit()
