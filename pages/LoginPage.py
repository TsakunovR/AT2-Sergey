from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//a[@data-l="t,login_tab"]')
    FIELD_LOGIN = (By.XPATH, '//a[@data-l="t,login_tab"]')
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

class LoginPageHelper(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.check_page()
    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB, 10)




