from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure

class LoginPageLocators:
    BUTTON_RECOVERY = (By.XPATH,'//button[@data-l="t,restore"]')
    BUTTON_CANCEL = (By.XPATH, '//a[@data-l="t,cancel"]')
    TEXT_SUPPORT_SRVICE = (By.XPATH, '//div[@class="external-oauth-login-help portlet_f"]')
    WARNING_TEXT = (By.XPATH, '//div[@class="stub"]')

class LoginPageHelperPasswordRecovery(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.check_page()

    @allure.step('Проверяем наличие всех элементов на странице восстановления профиля')
    def check_page(self):
        self.find_element(LoginPageLocators.BUTTON_RECOVERY)
        self.find_element(LoginPageLocators.BUTTON_CANCEL)
        self.find_element(LoginPageLocators.TEXT_SUPPORT_SRVICE)
        self.find_element(LoginPageLocators.WARNING_TEXT)
