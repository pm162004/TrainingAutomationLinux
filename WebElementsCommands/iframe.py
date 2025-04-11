from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.get("https://selectorshub.com/iframe-scenario/")
time.sleep(2)
# Wait for the iframe to be present
iframe = driver.find_element(By.XPATH,"//iframe[@id='pact1']")


driver.switch_to.frame(iframe)
driver.find_element(By.XPATH,"//input[@id='inp_val']").send_keys("priya")
driver.switch_to.default_content()


time.sleep(2)
