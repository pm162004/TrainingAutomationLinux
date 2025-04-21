from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    #Locators
    txtbox_username_id="Email"
    txtbox_password_id="Password"
    button_login_xpath="//button[normalize-space()='Log in']"

    #constructor
    def __init__(self,driver):
        self.driver=driver

    #action methods
    def setUserName(self,username):
        usernametxt=self.driver.find_element(By.ID,self.txtbox_username_id)
        usernametxt.clear()
        usernametxt.send_keys(username)

    def setPassword(self,pwd):
        passwordtxt=self.driver.find_element(By.ID,self.txtbox_password_id)
        passwordtxt.clear()
        passwordtxt.send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()