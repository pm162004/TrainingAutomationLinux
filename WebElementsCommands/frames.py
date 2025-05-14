from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# Code not working
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://yopmail.com/en/wm")

try:
    # Wait up to 10 seconds for the frame to be available
    wait = WebDriverWait(driver, 10)
    frame = wait.until(EC.frame_to_be_available_and_switch_to_it("ifmail"))
    
    # Wait for the link to be clickable
    booking_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'View My Booking')))
    booking_link.click()
    
    # Switch back to default content
    driver.switch_to.default_content()

except TimeoutException:
    print("Frame or element not found within the specified time")
finally:
    driver.quit()