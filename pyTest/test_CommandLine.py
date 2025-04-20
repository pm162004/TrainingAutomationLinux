from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCLI:
    def test_Login(self,setup):
        self.driver=setup
        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        try:
            self.status = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False