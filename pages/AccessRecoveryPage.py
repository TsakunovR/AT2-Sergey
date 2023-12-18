from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure

class AccessRecoveryPageLocators:
    BUTTON_PHONE = (By.XPATH, '//a[@data-l="t,phone"]')
    BUTTON_EMAIL = (By.XPATH, '//a[@data-l="t,email"]')
    BUTTON_SUPPORT = (By.XPATH, '//a[@data-l="t,support"]')

class AccessRecoveryPageHelper(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.check_page()

    def check_page(self):
            self.find_element(AccessRecoveryPageLocators.BUTTON_PHONE)
            self.find_element(AccessRecoveryPageLocators.BUTTON_EMAIL)
            self.find_element(AccessRecoveryPageLocators.BUTTON_SUPPORT)

    def clickPhoneButton(self):
        self.find_element(AccessRecoveryPageLocators.BUTTON_PHONE).click()

    def clickEmailButton(self):
        self.find_element(AccessRecoveryPageLocators.BUTTON_EMAIL).click()

    def clickSupportButton(self):
        self.find_element(AccessRecoveryPageLocators.BUTTON_SUPPORT).click()
