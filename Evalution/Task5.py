from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def drag_and_drop_demo():

    driver = webdriver.Chrome()


    driver.get("http://demo.guru99.com/test/drag_drop.html")
    driver.maximize_window()


    time.sleep(2)


    source = driver.find_element(By.XPATH, "//a[text()=' BANK ']")
    target = driver.find_element(By.ID, "bank")


    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()


    time.sleep(2)


    source_amount = driver.find_element(By.XPATH, "//a[text()=' 5000 ']")
    target_amount = driver.find_element(By.ID, "amt7")
    actions.drag_and_drop(source_amount, target_amount).perform()

    time.sleep(2)


    driver.quit()

drag_and_drop_demo()
