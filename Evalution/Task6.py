from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_and_capture_tooltip():
    # Set up the WebDriver
    driver = webdriver.Chrome()

    # Open the demo site
    driver.get("https://demoqa.com/tool-tips")
    driver.maximize_window()

    # Wait for the page to load
    time.sleep(2)

    # Locate the button with tooltip
    tooltip_button = driver.find_element(By.ID, "toolTipButton")

    # Hover over the button using ActionChains
    actions = ActionChains(driver)
    actions.move_to_element(tooltip_button).perform()

    # Wait for the tooltip to appear
    time.sleep(1)

    # Capture the tooltip text
    tooltip_text_element = driver.find_element(By.CLASS_NAME, "tooltip-inner")
    tooltip_text = tooltip_text_element.text

    print(f"Tooltip Text: {tooltip_text}")

    # Close the browser
    driver.quit()

# Run the test
hover_and_capture_tooltip()
