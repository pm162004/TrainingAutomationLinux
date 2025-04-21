from Opencart.PageObjects.HomePage import HomePage
from Opencart.PageObjects.AccountRegistrationPage import AccountRegistrationPage
from Opencart.utilities.randomeString import random_string_generator


class Test_AccountReg:
    baseURL = "https://demo.opencart.com.gr/"

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

        self.regpage.setEmail(self.email)
        # self.regpage.setEmail("tes@159gmail.com")
        self.regpage.setTphone("7878787878")
        self.regpage.setPassword("abc@123")
        self.regpage.setConfirm("abc@123")
        self.regpage.setNewsletter()
        self.regpage.setAgree()
        self.regpage.clickContinue()

        self.ConfirmMsg = self.regpage.getSuccessMsg()
        self.hp.clickLogOut()
        # self.hp.clickLogOut()
        self.driver.close()

        if self.ConfirmMsg=="Congratulations! Your new account has been successfully created!":

            assert True
        else:
            assert False
