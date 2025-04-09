

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/frames.php")
time.sleep(2)
driver.switch_to.frame("//iframe[@src='new-tab-sample.php']")
driver.find_element(By.LINK_TEXT,'Selenium - Automation Practice Form')
driver.switch_to.default_content()
