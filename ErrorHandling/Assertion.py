from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    print("Waiting for the button...")

    # Fallback to XPath for the Google Search button
    button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='btnK']"))
    )
    print("Button found!")

    # Check if the button is displayed
    assert button.is_displayed(), "Button is missing!"
    print("Button is visible!")

except TimeoutException:
    print("The element was not found within the given time.")
except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
