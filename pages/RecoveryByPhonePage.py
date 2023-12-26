from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure

class RecoveryByPhonePageLocator:
    FIELD_PHONE_NUMBER = (By.XPATH,'//div[@data-l="t,phone"]')
    COUNTRY_FIELD = (By.XPATH,'//div[@data-l="t,country"]')
    COUNTRY_LIST_ITEM = (By.XPATH,'//div[@class="country-select_i"]')
    BUTTON_GET_THE_CODE =(By.XPATH,'//input[@data-l="t,submit"]')
    ATRIBUTE_FIELD_PHONE_CODE = (By.XPATH, '//input[@id="field_phone"]')

class RecoveryByPhonePageHelper(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.check_page()

    def check_page(self):
        self.find_element(RecoveryByPhonePageLocator.FIELD_PHONE_NUMBER)
        self.find_element(RecoveryByPhonePageLocator.COUNTRY_FIELD)
        self.find_element(RecoveryByPhonePageLocator.BUTTON_GET_THE_CODE)

    def select_country(self, country_number):
        self.find_element(RecoveryByPhonePageLocator.COUNTRY_FIELD).click()
        country_list_item = self.find_elements(RecoveryByPhonePageLocator.COUNTRY_LIST_ITEM)[country_number]
        country_name = country_list_item.get_attribute('data-name')
        country_code_element = (By.XPATH, f'//div[@data-name="{country_name}"]//div[@class="country-select_code"]')
        country_code = self.find_element(country_code_element).text
        country_list_item.click()
        return country_code

    def get_phone_code_from_field(self):
        phone_code = self.find_element(RecoveryByPhonePageLocator.ATRIBUTE_FIELD_PHONE_CODE).get_attribute('value')
        return phone_code











