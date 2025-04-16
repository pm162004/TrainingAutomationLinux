from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def drag_and_drop_demo():
    # Set up the WebDriver (make sure chromedriver is in your PATH)
    driver = webdriver.Chrome()

    # Open the demo site
    driver.get("http://demo.guru99.com/test/drag_drop.html")
    driver.maximize_window()

    # Wait for the page to load
    time.sleep(2)

    # Locate source and target elements
    source = driver.find_element(By.XPATH, "//a[text()=' BANK ']")
    target = driver.find_element(By.ID, "bank")

    # Perform drag and drop using ActionChains
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    # Pause to see the result
    time.sleep(2)

    # You can repeat this for other elements too, e.g.
    source_amount = driver.find_element(By.XPATH, "//a[text()=' 5000 ']")
    target_amount = driver.find_element(By.ID, "amt7")
    actions.drag_and_drop(source_amount, target_amount).perform()

    time.sleep(2)

    # Close the browser
    driver.quit()

# Run the demo
drag_and_drop_demo()
