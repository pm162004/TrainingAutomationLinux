import pytest

from Opencart.PageObjects.HomePage import HomePage
from Opencart.PageObjects.AccountRegistrationPage import AccountRegistrationPage
from Opencart.utilities.randomeString import random_string_generator
import os

from Opencart.utilities.readProperties import ReadConfig
from Opencart.utilities.customLogger import LogGen

class Test_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_account_reg(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFname("Priya")
        self.regpage.setLname("Modi")
        # Generate a random email without `self`
        self.email = random_string_generator() + '@gmail.com'
        print(self.email)
        #
        self.regpage.setEmail(self.email)
        # self.regpage.setEmail("abcxyz76iii810@gmail.com")
        # self.regpage.setEmail("tes@159gmail.com")
        self.regpage.setTphone("7878787878")
        self.regpage.setPassword("abc@123")
        self.regpage.setConfirm("abc@123")
        self.regpage.setNewsletter()
        self.regpage.setAgree()
        self.regpage.clickContinue()

        self.ConfirmMsg = self.regpage.getSuccessMsg()
        # self.hp.clickLogOut()
        # self.hp.clickLogOut()


        if self.ConfirmMsg=="Congratulations! Your new account has been successfully created!":

            assert True

            self.driver.close()
        else:
            screenshots_dir = os.path.join(os.path.abspath(os.curdir), "screenshots")
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)
            screenshot_path = os.path.join(screenshots_dir, "2test_account_reg.png")
            self.driver.save_screenshot(screenshot_path)
            # Ensure the 'screenshots' directory exists
            # if not os.path.exists(os.path.join(os.curdir, "screenshots")):
            #     os.makedirs(os.path.join(os.curdir, "screenshots"))
            #
            # # Save the screenshot
            # self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "1test_account_reg.png")

            # self.driver.save_screenshot('/home/web-h-028/PycharmProjects/TrainingAutomation/Opencart/screenshots/reg.png')

            self.driver.close()
            assert False
