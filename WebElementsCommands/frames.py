from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.get("https://in.search.yahoo.com/?fr2=inr")
driver.maximize_window()
time.sleep(2)