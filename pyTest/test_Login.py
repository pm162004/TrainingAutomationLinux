from selenium import webdriver

from LoginPageObjects import LoginPage

class TestLogin:
    def test_login(self):

        self.driver=webdriver.Chrome()
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName("admin@yourstore.com")
        self.lp.setPassword("admin")
        self.lp.clickLogin()
        self.act_title=self.driver.title
        print(self.act_title)
        print(self.driver.title)
        self.driver.close()
        assert self.act_title == "Just a moment..."




