from Opencart.PageObjects.HomePage import HomePage
from Opencart.PageObjects.AccountRegistrationPage import AccountRegistrationPage

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
        # self.email = randomeString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail("test@12gmail.com")
        self.regpage.setTphone("7878787878")
        self.regpage.setPassword("abc@123")
        self.regpage.setConfirm("abc@123")
        self.regpage.setNewsletter()
        self.regpage.setAgree()
        self.regpage.clickContinue()
        self.ConfirmMsg = self.regpage.getSuccessMsg()
        self.driver.close()
        if self.ConfirmMsg=="":
            assert True
        else:
            assert False