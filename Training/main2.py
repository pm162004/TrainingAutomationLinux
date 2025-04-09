from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://riddhi-gsp-admin-dev.webelight.co.in/sign-in")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='Phone']").send_keys("7070707070")
#print(name)
driver.find_element(By.NAME,"password").send_keys("0000")
driver.find_element(By.CLASS_NAME,"button").click()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.refresh()
# driver.close()