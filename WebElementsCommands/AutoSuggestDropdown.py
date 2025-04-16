from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
# drop = driver.find_element(By.ID,"exampleFormControlSelect1")
# time.sleep(2)
# driver.find_element(By.XPATH,"//option[normalize-space()='Female']").click()
# time.sleep(5)

driver.find_element(By.ID,"autosuggest").send_keys("In")
# drop.select_by_index(0)
# drop.select_by_visible_text("Female")
time.sleep(2)
country=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']  a")
print(len(country))
for cou in country:
    if cou.text == "India":
        cou.click()

time.sleep(2)

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"