from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

firefox_options = Options()
service = Service(executable_path='/snap/bin/geckodriver')

driver = webdriver.Firefox(service=service, options=firefox_options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
print(driver.title)

driver.quit()
