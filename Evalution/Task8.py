from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

actions = ActionChains(driver)


input_box = driver.find_element(By.ID, "name")
input_box.send_keys(" Test")

input_box.send_keys(Keys.ENTER)
time.sleep(1)


input_box.click()
actions.send_keys(Keys.TAB).perform()


input_box.send_keys("abc")
time.sleep(1)
input_box.send_keys(Keys.BACKSPACE * 3)

input_box.send_keys("Copied Text")
input_box.send_keys(Keys.CONTROL, 'a')  # Select all
input_box.send_keys(Keys.CONTROL, 'c')  # Copy
time.sleep(1)
input_box.send_keys(Keys.CONTROL, 'v')  # Paste

# ===== Scrolling Down using PAGE_DOWN =====
actions.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)


actions.send_keys(Keys.PAGE_UP).perform()
time.sleep(1)


actions.send_keys(Keys.F5).perform()


time.sleep(3)
driver.quit()
