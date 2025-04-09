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


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Set up Firefox options
options = Options()
options.set_preference("profile", "/home/web-h-028/snap/firefox/common/.mozilla/firefox/2dirgxlq.priya")  # Set your profile path here

# Initialize the Firefox driver with options
driver = webdriver.Firefox(options=options)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.close()
