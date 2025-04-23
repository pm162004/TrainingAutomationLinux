
from Opencart.PageObjects.HomePage import HomePage
from Opencart.PageObjects.LoginPage import LoginPage
from Opencart.PageObjects.AccountRegistrationPage import AccountRegistrationPage
from Opencart.utilities.randomeString import random_string_generator
import os
import urllib3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Opencart')))

from Opencart.utilities.readProperties import ReadConfig
from Opencart.utilities.customLogger import LogGen
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Test_Login():


    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    user1 = ReadConfig.getUseremail1()
    password1 = ReadConfig.getPassword1()

    user2 = ReadConfig.getUseremail2()
    password2 = ReadConfig.getPassword2()

    user3 = ReadConfig.getUseremail3()
    password3 = ReadConfig.getPassword3()



    def test_login2(self):
            self.logger.info("******* Starting test_002_login **********")

            self.driver.get(self.baseURL)
            self.driver.maximize_window()

            self.hp = HomePage(self.driver)
            self.hp.clickMyAccount()
            self.hp.clickLogin()



            self.lp = LoginPage(self.driver)
            self.lp.setEmail(self.user1)
            self.lp.setPassword(self.password1)
            self.lp.clickLogin()


            self.targetpage = self.lp.IsAccountPageExists()
            if self.targetpage == True:
                assert True
            else:
                self.driver.save_screenshot("screenshots/test_002_login.png")
                assert False

            self.driver.close()
            self.logger.info("******* End of test_002_login **********")

    def test_login3(self):
        self.logger.info("******* Starting test_002_login **********")

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user2)
        self.lp.setPassword(self.password2)
        self.lp.clickLogin()



        self.targetpage = self.lp.IsAccountPageExists()
        if self.targetpage == True:
            assert True
        else:
            self.driver.save_screenshot("screenshots/test_002_login.png")
            assert False

        self.driver.close()
        self.logger.info("******* End of test_002_login **********")

    def test_login4(self):
        self.logger.info("******* Starting test_002_login **********")

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()


        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user3)
        self.lp.setPassword(self.password3)
        self.lp.clickLogin()

        self.targetpage = self.lp.IsAccountPageExists()
        if self.targetpage == True:
            assert True
        else:
            self.driver.save_screenshot("screenshots/test_002_login.png")
            assert False

        self.driver.close()
        self.logger.info("******* End of test_002_login **********")

    def test_login(self):
        self.logger.info("******* Starting test_002_login **********")

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()


        self.targetpage=self.lp.IsAccountPageExists()
        if self.targetpage==True:
            assert True
        else:
            self.driver.save_screenshot("screenshots/test_002_login.png")
            assert False

        self.driver.close()
        self.logger.info("******* End of test_002_login **********")