from selenium.webdriver.common.by import By
class HomePage():
    link_myaccount_xpath = "//a[normalize-space()='Your Store']"
    link_register_linktest = "Register"
    link_login_linktest = "Login"

    def __init__(self,driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.link_myaccount_xpath)

    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.link_register_linktest).click()
        
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.link_login_linktest).click()