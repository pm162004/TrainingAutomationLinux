from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.get("https://in.search.yahoo.com/?fr2=inr")
driver.maximize_window()
time.sleep(2)
count = driver.find_elements(By.TAG_NAME,'a')
print(count)
print("The total links are there in the website is",len(count))
# driver.find_element(By.PARTIAL_LINK_TEXT,'CWC Meet').click()