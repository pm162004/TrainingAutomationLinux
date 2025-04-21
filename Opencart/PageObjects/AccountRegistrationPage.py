from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AccountRegistrationPage():
    text_fname_name = "firstname"
    text_lname_name = "lastname"
    text_email_name = "email"
    text_tphone_name = "telephone"
    text_password_name = "password"
    text_confirm_name = "confirm"
    radio_newsletter_name = "newsletter"
    check_policy_name = "agree"
    button_continue_xpath = "//input[@value='Continue']"
    message_sucess_xpath = "//p[contains(text(),'Congratulations! Your new account has been successfully created!')]"

    def __init__(self, driver):
        self.driver = driver

    def setFname(self,fname):
        self.driver.find_element(By.NAME, self.text_fname_name).send_keys(fname)

    def setLname(self,lname):
        self.driver.find_element(By.NAME, self.text_lname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME, self.text_email_name).send_keys(email)

    def setTphone(self,tphone):
        self.driver.find_element(By.NAME, self.text_tphone_name).send_keys(tphone)

    def setPassword(self,password):
        self.driver.find_element(By.NAME, self.text_password_name).send_keys(password)

    def setConfirm(self,confirm):
        self.driver.find_element(By.NAME, self.text_confirm_name).send_keys(confirm)

    def setNewsletter(self):
        self.driver.find_element(By.NAME, self.radio_newsletter_name).click()

    def setAgree(self):
        self.driver.find_element(By.NAME, self.check_policy_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.button_continue_xpath).click()

    def getSuccessMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.message_sucess_xpath).text
        except:
            None