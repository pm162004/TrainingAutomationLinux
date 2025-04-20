from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def google_search(keyword):

    driver = webdriver.Chrome()


    driver.get("https://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)




    results = driver.find_elements(By.CSS_SELECTOR, "h3")[:5]

    print("\nTop 5 search results:")
    for i, result in enumerate(results, start=1):
        print(f"{i}. {result.text}")


    driver.quit()



google_search("AI")