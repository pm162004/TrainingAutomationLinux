from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def google_search(keyword):
    # Set up the WebDriver (make sure to download the right ChromeDriver version)
    driver = webdriver.Chrome()

    # Open Google
    driver.get("https://www.google.com")

    # Find the search box and enter the keyword
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(9)


    results = driver.find_elements(By.CSS_SELECTOR, "h3")[:5]

    print("\nTop 5 search results:")
    for i, result in enumerate(results, start=1):
        print(f"{i}. {result.text}")

    # Close the browser
    driver.quit()


# Example usage
google_search("OpenAI ChatGPT")
