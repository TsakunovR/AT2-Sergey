from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//a[@data-l="t,login_tab"]')
    FIELD_LOGIN = (By.XPATH, '//input[@data-l="t,login"]')
    FIELD_PASSWORD = (By.XPATH, '//input[@data-l="t,password"]')
    SIGN_IN_BUTTON = (By.XPATH, '//input[@data-l="t,sign_in"]')
    SIGN_IN_BUTTON_QR = (By.XPATH, '//a[@data-l="t,get_qr"]')
    CANT_SIGN_IN = (By.XPATH, '//a[@data-l="t,restore"]')
    REGISTRATION = (By.XPATH, '//a[@data-l="t,register"]')
    VK_BUTTON = (By.XPATH, '//a[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//a[@data-l="t,mailru"]')
    GOOGLE_BUTTON = (By.XPATH, '//a[@data-l="t,google"]')
    YANDEX_BUTTON = (By.XPATH, '//a[@data-l="t,yandex"]')
    APPLE_BUTTON = (By.XPATH, '//a[@data-l="t,apple"]')
    QR_TAB = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    ERROR_FIELD_TEXT = (By.XPATH, '//div[@class="form_i form_i__error"]')

class LoginPageHelper(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.check_page()
    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB, 10)
    def cliclLoginBatton(self):
        self.find_element(LoginPageLocators.SIGN_IN_BUTTON).click()
    def getErrorText(self):
        return self.find_element(LoginPageLocators.ERROR_FIELD_TEXT).text
    def set_login(self, login):
        self.find_element(LoginPageLocators.FIELD_LOGIN).send_keys(login)
    def set_password(self,password):
        self.find_element(LoginPageLocators.FIELD_PASSWORD).send_keys(password)




