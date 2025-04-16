from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome() #Launch The Browser
driver.get("https://www.automationexercise.com/products")  # Open the website
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.NAME, 'search').send_keys("women")

time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='submit_search']").click()

time.sleep(2)

driver.find_element(By.XPATH, "//a[normalize-space()='Add to cart']").click()

time.sleep(2)
driver.get("https://www.automationexercise.com/view_cart")
driver.find_element(By.XPATH, "//a[normalize-space()='Proceed To Checkout']").click()

time.sleep(2)
driver.close()