from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure

class AgreementsAndPoliciesPageLocator:
    RULES = (By.XPATH,'//div[@class="rules_links"]')
    FAQ = (By.XPATH, '//ul[@class="faq_ul"]')

class AgreementsAndPoliciesHelper(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.check_page()

    @allure.step('Проверяем наличие всех элементов на странице "Соглашения и политики"')
    def check_page(self):
        self.find_element(AgreementsAndPoliciesPageLocator.RULES)
        self.find_element(AgreementsAndPoliciesPageLocator.FAQ)