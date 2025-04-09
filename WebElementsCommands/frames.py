from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.get("https://yopmail.com/en/wm")
time.sleep(2)
driver.switch_to.frame("ifmail")
driver.find_element(By.LINK_TEXT,'View My Booking').click()
driver.switch_to.default_content()


