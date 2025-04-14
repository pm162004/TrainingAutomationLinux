from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# Start the driver
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://safarr-admin-dev.webelight.co.in/sign-in")
driver.maximize_window()

# Login with blank inputs (this is an invalid login case)
driver.find_element(By.NAME,"email").send_keys("")
driver.find_element(By.NAME,"password").send_keys("")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0) # blank inputs

# # Assert that an error message appears due to blank inputs
# error_message = driver.find_element(By.XPATH, "//div[contains(text(),'Email is required.')] AND //div[contains(text(),'Email is required.')]")
# assert "Invalid" in error_message.text, "Error message not found"

adminUname = driver.find_element(By.NAME,"email")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("admin@gmail.com")
adminUpass = driver.find_element(By.NAME,"password")
adminUpass.send_keys(Keys.CONTROL,"a")
adminUpass.send_keys(Keys.DELETE)
adminUpass.send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0) # wrong password

adminUname = driver.find_element(By.NAME,"email")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("admin1@gmail.com")
adminUpass = driver.find_element(By.NAME,"password")
adminUpass.send_keys(Keys.CONTROL,"a")
adminUpass.send_keys(Keys.DELETE)
adminUpass.send_keys("Admin@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0) # wrong email

adminUname = driver.find_element(By.NAME,"email")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("admin1@gmail.com")
adminUpass = driver.find_element(By.NAME,"password")
adminUpass.send_keys(Keys.CONTROL,"a")
adminUpass.send_keys(Keys.DELETE)
adminUpass.send_keys("Admin@12")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0) # wrong email password

# Login with correct credentials
adminUname = driver.find_element(By.NAME,"email")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("admin@gmail.com")
adminUname = driver.find_element(By.NAME,"password")
adminUname.send_keys(Keys.CONTROL,"a")
adminUname.send_keys(Keys.DELETE)
adminUname.send_keys("Admin@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()  # login
time.sleep(3.0)
driver.forward()

driver.get("https://safarr-admin-dev.webelight.co.in/truth-or-truth")
time.sleep(3.0)   # select the truth or truth menu
sel = driver.find_element(By.XPATH,"(//*[contains(text(),'Add Question')])[1]")
driver.execute_script("arguments[0].click();",sel)
time.sleep(3.0) # Add the question

input_element = driver.find_element(By.XPATH, "(//input[@placeholder='Enter Question'])[1]")
 # This clears any existing text in the input field
input_element.click()
input_element.send_keys(Keys.CONTROL + "a")  # or Keys.COMMAND + "a" on macOS
input_element.send_keys(Keys.DELETE)
# Then send new text
random_number = random.randint(100000, 999999)
input_element.send_keys("New User"+str(random_number))
time.sleep(3) # write the question

driver.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click()
time.sleep(3) # Click the save button

toggles = driver.find_elements(By.CLASS_NAME, "switcher-toggle")  # finds all
toggles[0].click() # toggle

driver.find_element(By.XPATH,"(//button[normalize-space()='Confirm'])[1]").click()
time.sleep(2) # CONFIRM

driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]/div[1]/span[2]/button[1]").click()
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
random_number = random.randint(100000, 999999)
input_element.send_keys("Test User 2"+str(random_number))

time.sleep(3) # write the question
driver.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click()
time.sleep(3) # Click the save button
button = driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]/div[1]/span[3]")
button.click()
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
random_number = random.randint(100000, 999999)
input_element.send_keys("how are uuu"+str(random_number))

time.sleep(3) # write the question
driver.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click()
time.sleep(3) # Click the save button
driver.close()