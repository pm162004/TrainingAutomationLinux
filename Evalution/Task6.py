from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_and_capture_tooltip():

    driver = webdriver.Chrome()


    driver.get("https://demoqa.com/tool-tips")
    driver.maximize_window()


    time.sleep(2)


    tooltip_button = driver.find_element(By.ID, "toolTipButton")


    actions = ActionChains(driver)
    actions.move_to_element(tooltip_button).perform()

    time.sleep(1)

    tooltip_text_element = driver.find_element(By.CLASS_NAME, "tooltip-inner")
    tooltip_text = tooltip_text_element.text

    print(f"Tooltip Text: {tooltip_text}")


    driver.quit()


hover_and_capture_tooltip()
