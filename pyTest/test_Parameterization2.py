import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestClass:
    @pytest.mark.parametrize('user,pwd',
                             [("Admin","admin123"),
                              ("adm","admin123"),
                              ("Admin","adm"),
                              ("adm","adm")
                              ]
                             )
    def test_Login(self,user,pwd):
        self.driver=webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.NAME, "username").send_keys(user)
        self.driver.find_element(By.NAME, "password").send_keys(pwd)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        try:
            self.status=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status==True
        except:
            self.driver.close()
            assert False


