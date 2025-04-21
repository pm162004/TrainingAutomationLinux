from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def main():
    # Get the geckodriver executable path using GeckoDriverManager
    geckodriver_path = GeckoDriverManager().install()

    # Initialize the Firefox service
    service = Service(geckodriver_path)

    # Set up Firefox options (if needed)
    options = webdriver.FirefoxOptions()
    options.headless = True  # If you want the browser to run in headless mode

    # Initialize the Firefox WebDriver
    driver = webdriver.Firefox(service=service, options=options)

    # Navigate to Google
    driver.get("https://www.google.com")

    # Print the title of the page
    print(driver.title)

    # Quit the driver
    driver.quit()


if __name__ == "__main__":
    main()

