from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
print("Hello")
time.sleep(5)
# https://www.guru99.com/xpath-selenium.html
# python -m pytest -s -v --html=reports\report.html --capture=tee-sys OpenCart\testCases\test_LoginPage1.py