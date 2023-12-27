from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure

class RegistrationPageLocator:
    FIELD_PHONE_NUMBER = (By.XPATH,'//div[@data-l="t,phone"]')
    FIELD_COUNTRY = (By.XPATH, '//div[@data-l="t,country"]')
    FURTHER_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')
    REGULATION_TEXT = (By.XPATH, '//a[@data-l="t,agreement"]')
    PRIVACY_POLICY_TEXT = (By.XPATH,'//a[@data-l="t,privacy"]')
    TEXT_ERROR_EMPTY_FIELD_PHONE = (By.XPATH, '//div[@class="input-e js-ph-vl-hint"]')

class RegistrationPageHelper(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.check_page()

    @allure.step('Проверяем наличие всех элементов на странице  регистрации')
    def check_page(self):
        self.find_element(RegistrationPageLocator.FIELD_PHONE_NUMBER)
        self.find_element(RegistrationPageLocator.FIELD_COUNTRY)
        self.find_element(RegistrationPageLocator.FURTHER_BUTTON)
        self.find_element(RegistrationPageLocator.REGULATION_TEXT)
        self.find_element(RegistrationPageLocator.PRIVACY_POLICY_TEXT)

    @allure.step('Нажимаем кнопку далее')
    def click_further_button(self):
        self.find_element(RegistrationPageLocator.FURTHER_BUTTON).click()

    @allure.step('Проверяем текст ошибки при пустом поле телефон')
    def getTextError(self):
        return self.find_element(RegistrationPageLocator.TEXT_ERROR_EMPTY_FIELD_PHONE).text