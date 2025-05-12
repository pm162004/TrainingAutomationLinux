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

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def login_password():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def refresh_page():
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait for the body to load after refresh

def MyFilesPage():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def myShrubs():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='My Shrubs']")))

def new_shrub():
    return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".md-button-content")))

def shrubs_title_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "shrub-name")))

def shrubs_title_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Shrub Title is required']")))

def shrubs_Permissions_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Permissions field is required']")))

def shrubs_Thumbnail_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Thumbnail type field is required']")))

def shrubs_btn():
    return wait.until(EC.element_to_be_clickable((By.NAME, "btn-save")))

def show_title():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Do you want to show the title?']")))

def shrubs_view_only():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='View Only']")))

def hide_thumbnail():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Do you want to show thumbnail?']")))

def select_type():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Shrub Project Icon']")))

def select_icon():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//h6[normalize-space()='alert-octagon']")))

def close_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Cancel')]")))

def test_login():

    email_input_field().send_keys(email)
    login_password().send_keys(password)
    btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
    btn_login.click()
    assert MyFilesPage().text == validation_assert.MY_FILES

def test_myShrubs():
    myShrubs().click()
    time.sleep(10)
    new_shrub().click()

def test_blank_shrubs():
    shrubs_btn().click()
    assert shrubs_title_validation().text == validation_assert.ENTER_SHRUBS_TITLE
    assert shrubs_Permissions_validation().text == validation_assert.ENTER_SHRUBS_PERMISSIONS
    assert shrubs_Thumbnail_validation().text == validation_assert.ENTER_SHRUBS_THUMBNAIL

def test_valid_shrubs():
    refresh_page()
    shrubs_title_input_field().send_keys(input_field.VALID_SHRUBS)
    # show_title().click()
    shrubs_btn().click()
    shrubs_view_only().click()
    # hide_thumbnail().click()
    select_type().click()
    select_icon().click()
    close_btn().click()
    shrubs_btn().click()
    # time.sleep(10)
