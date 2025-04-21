import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestLogin:
    def test_login_chrome(self):


        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()  # Signin
        assert self.driver.title == "OrangeHRM"

        self.driver.quit()


    def test_login_edge(self):
        self.driver = webdriver.Edge()

        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    def test_login_firefox(self):
        self.driver = webdriver.Firefox()

        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

