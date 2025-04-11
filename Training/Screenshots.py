from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/')
driver.save_screenshot(r'C:\Users\WEB-H-051\Desktop\Automation\ScriptsScreenshots\homepage.png')
time.sleep(2)
driver.find_element(By.NAME, "q").send_keys("LinkedIn login")
driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)

driver.save_screenshot(r'\home\web-h-028\PycharmProjects\TrainingAutomation\Training\s1.png')

# driver.get_screenshot_as_file(r'\home\web-h-028\PycharmProjects\TrainingAutomation\Training\s1.png')
time.sleep(2)
driver.close()
