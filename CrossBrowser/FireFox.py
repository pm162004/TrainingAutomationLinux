from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

# Specify the correct path to your Firefox profile
profile_path = "/home/web-h-028/PycharmProjects/TrainingAutomation/webbrowser"

# Set Firefox options
options = Options()
options.headless = True  # Set to True for headless mode if needed

# Load the profile
profile = FirefoxProfile(profile_path)

# Set the profile in the options
options.profile = profile

# Set up the service for geckodriver
service = Service(executable_path='/home/web-h-028/PycharmProjects/TrainingAutomation/webbrowser/geckodriver')
options.log.level = "trace"

# Initialize the Firefox WebDriver with profile and options
driver = webdriver.Firefox(service=service, options=options)

# Open Google
driver.get("https://www.google.com/")

# Close the browser
driver.quit()




# from selenium import webdriver
# import time
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
#
# options = Options()
# options.headless = True  # Set headless if required
#
# service = Service(executable_path='/home/web-h-028/PycharmProjects/TrainingAutomation/webbrowser/geckodriver')
#
# driver = webdriver.Firefox(service=service, options=options)
#
#
# driver.get("https://www.google.com/")
# driver.maximize_window()
# time.sleep(5)
#





from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
#
# # Create a FirefoxProfile instance
# profile = FirefoxProfile("/home/web-h-028/snap/firefox/common/.mozilla/firefox/dagmbq7e.default")
#
# # Use the profile with Firefox WebDriver
# driver = webdriver.Firefox(firefox_profile=profile)
# driver.get("https://www.google.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.close()


# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
#
# # Set up Firefox options
# options = Options()
# options.set_preference("profile", "/home/web-h-028/snap/firefox/common/.mozilla/firefox/2dirgxlq.priya")  # Set your profile path here
#
# # Initialize the Firefox driver with options
# driver = webdriver.Firefox(options=options)
# driver.get("https://www.google.com/")
# driver.maximize_window()
# driver.close()
