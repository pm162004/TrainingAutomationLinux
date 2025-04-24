from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from Opencart.PageObjects.HomePage import HomePage
from Opencart.PageObjects.LoginPage import LoginPage
from Opencart.PageObjects.MyAccountPage import MyAccountPage
from Opencart.utilities import XLUtils
from Opencart.utilities.readProperties import ReadConfig
from Opencart.utilities.customLogger import LogGen



class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger
    path = "/home/web-h-028/PycharmProjects/TrainingAutomation/Opencart/testdata/Opencart_LoginData.xlsx"

    def test_login_ddt(self, setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)

        for r in range(2, self.rows + 1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            # Use explicit wait for the email field to be visible
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='input-email']")))
            self.driver.refresh()
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()


            # Wait for the page to load after clicking login
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='My Account']")))  # Adjust to an element that confirms login success
            self.hp.clickLogin()
            self.targetpage = self.lp.IsAccountPageExists()

            if self.exp == 'Valid':
                if self.targetpage:
                    lst_status.append('Pass')
                    self.ma.clickLogOut()
                    self.driver.refresh()
                else:
                    lst_status.append('Fail')
                    self.ma.clickLogin()
            elif self.exp == 'Invalid':
                if self.targetpage:
                    lst_status.append('Fail')
                    self.ma.clickLogOut()
                    # self.hp = HomePage(self.driver)
                    # self.hp.clickMyAccount()
                    # self.hp.clickLogin()
                    # self.hp.clickLogin()
                    # self.driver.refresh()
                    # self.ma.clickLogin()
                    # self.driver.refresh()
                else:
                    lst_status.append('Pass')

        self.driver.close()

        if "Fail" not in lst_status:
            assert True
        else:
            assert False

        self.logger.info("******* End of test_003_login_Datadriven **********")
