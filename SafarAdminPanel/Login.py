
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://safarr-admin-dev.webelight.co.in/sign-in")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("admin@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Admin@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0)
driver.forward()
driver.get("https://safarr-admin-dev.webelight.co.in/truth-or-truth")
time.sleep(3.0)   # select the truth or truth menu
driver.find_element(By.XPATH,"(//label)[2]").click()
time.sleep(2)  # active status
driver.find_element(By.XPATH,"(//button[normalize-space()='Confirm'])[1]").click()
time.sleep(2) # CONFIRM
driver.find_element(By.XPATH,"//tbody/tr[2]/td[2]/div[1]/span[2]/button[1]//*[name()='svg']").click()
time.sleep(3.0)   # Edit Button


driver.find_element(By.XPATH,"(//div[@class='select__control css-15bhs5i-control'])[1]").click()


time.sleep(3.0) # open the dropdown
sel = driver.find_element(By.XPATH,"(//*[contains(text(),'English')])[1]")
driver.execute_script("arguments[0].click();",sel)

time.sleep(3.0) # select the english
driver.find_element(By.XPATH,"(//button[normalize-space()='Submit'])[1]").click()
time.sleep(3.0) # submit button
input_element = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Question'])[1]")
 # This clears any existing text in the input field
input_element.click()
input_element.send_keys(Keys.CONTROL + "a")  # or Keys.COMMAND + "a" on macOS
input_element.send_keys(Keys.DELETE)

# Then send new text
input_element.send_keys("Test User 2")

time.sleep(3) # write the question
driver.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click()
time.sleep(3) # Click the save button
driver.find_element(By.XPATH,"(//span[@class='tooltip-wrapper'])[7]").click()
time.sleep(3.0)   # Translate  Button



driver.find_element(By.XPATH,"(//div[@class='select__control css-15bhs5i-control'])[1]").click()

time.sleep(3.0) # open the dropdown
sel = driver.find_element(By.XPATH,"(//*[contains(text(),'Hindi')])[1]")
driver.execute_script("arguments[0].click();",sel)

time.sleep(3.0) # select the english
driver.find_element(By.XPATH,"(//button[normalize-space()='Submit'])[1]").click()
time.sleep(3.0)
input_element = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Question'])[1]")
 # This clears any existing text in the input field
input_element.click()
input_element.send_keys(Keys.CONTROL + "a")  # or Keys.COMMAND + "a" on macOS
input_element.send_keys(Keys.DELETE)

# Then send new text
input_element.send_keys("how are u")

time.sleep(3) # write the question
driver.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click()
time.sleep(3) # Click the save button
driver.close()
