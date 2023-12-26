from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure

class RecoveryByEmailPageLocator:
    GET_CODE_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')
    FIELD_MAIL = (By.XPATH, '//div[@data-l="t,email"]')
    ERROR_FIELD_TEXT = (By.XPATH, '//div[@class="input-e"]')

class RecoveryByEmailPageHelper(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.check_page()

    def check_page(self):
        self.find_element(RecoveryByEmailPageLocator.GET_CODE_BUTTON)
        self.find_element(RecoveryByEmailPageLocator.FIELD_MAIL)

    def cliclGetCodeButton(self):
        self.find_element(RecoveryByEmailPageLocator.GET_CODE_BUTTON).click()

    def getTextError(self):
        return self.find_element(RecoveryByEmailPageLocator.ERROR_FIELD_TEXT).text
