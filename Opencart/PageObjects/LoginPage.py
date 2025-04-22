from selenium.webdriver.common.by import By

class LoginPage():
    text_email_xpath = "//input[@id='input-email']"
    text_password_xpath = "//input[@id='input-password']"
    btn_login_xpath = "//input[@value='Login']"
    msg_login_xpath = "//h2[normalize-space()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()


    def IsAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_login_xpath).is_displayed()
        except:
            None