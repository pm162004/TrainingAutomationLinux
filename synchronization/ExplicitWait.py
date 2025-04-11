from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")

# Wait up to 10 seconds for the element to become clickable
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "alert2"))
)
button.click()
