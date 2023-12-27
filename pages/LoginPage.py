from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import allure
from selenium.webdriver.common.action_chains import ActionChains

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//a[@data-l="t,login_tab"]')
    FIELD_LOGIN = (By.XPATH, '//input[@data-l="t,login"]')
    FIELD_PASSWORD = (By.XPATH, '//input[@data-l="t,password"]')
    SIGN_IN_BUTTON = (By.XPATH, '//input[@data-l="t,sign_in"]')
    SIGN_IN_BUTTON_QR = (By.XPATH, '//a[@data-l="t,get_qr"]')
    CANT_SIGN_IN = (By.XPATH, '//a[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//a[@class="button-pro __sec mb-3x __wide"]')
    VK_BUTTON = (By.XPATH, '//a[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//a[@data-l="t,mailru"]')
    GOOGLE_BUTTON = (By.XPATH, '//a[@data-l="t,google"]')
    YANDEX_BUTTON = (By.XPATH, '//a[@data-l="t,yandex"]')
    APPLE_BUTTON = (By.XPATH, '//a[@data-l="t,apple"]')
    QR_TAB = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    ERROR_FIELD_TEXT = (By.XPATH, '//div[@class="form_i form_i__error"]')
    BUTTON_MORE = (By.XPATH,'//button[@class="more-popup_btn h-mod"]')
    BUTTON_AGREEMENTS_AND_POLICIES = (By.XPATH,'//a[text()="Соглашения и политики"]')



class LoginPageHelper(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.check_page()

    @allure.step('Проверяем наличие всех элементов на странице авторизации')
    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB, 10)
        self.find_element(LoginPageLocators.FIELD_LOGIN)
        self.find_element(LoginPageLocators.FIELD_PASSWORD)
        self.find_element(LoginPageLocators.SIGN_IN_BUTTON)
        self.find_element(LoginPageLocators.SIGN_IN_BUTTON_QR)
        self.find_element(LoginPageLocators.CANT_SIGN_IN)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.GOOGLE_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)
        self.find_element(LoginPageLocators.APPLE_BUTTON)
        self.find_element(LoginPageLocators.QR_TAB)

    @allure.step('Нажимаем на кнопку "Войти в одноклассники"')
    def cliclLoginBatton(self):
        self.find_element(LoginPageLocators.SIGN_IN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def getErrorText(self):
        return self.find_element(LoginPageLocators.ERROR_FIELD_TEXT).text

    @allure.step('Вводим логин')
    def set_login(self, login):
        self.find_element(LoginPageLocators.FIELD_LOGIN).send_keys(login)

    @allure.step('Вводим пароль')
    def set_password(self,password):
        self.find_element(LoginPageLocators.FIELD_PASSWORD).send_keys(password)

    @allure.step('Нажимаем на текст "Не получается войти"')
    def clicCantSignIn(self):
        self.find_element(LoginPageLocators.CANT_SIGN_IN).click()

    @allure.step('Нажимаем на кнопку "Зарегистрироваться"')
    def clicRegistrationButton(self):
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()

    @allure.step('Нажимаем на кнопку "еще" и выбираем в списке "Соглашения и политики"')
    def clicButtonMoreSelectAgreementsAndPolicies(self):
        BUTTON_MORE = self.find_element(LoginPageLocators.BUTTON_MORE)
        BUTTON_AGREEMENTS_AND_POLICIES = self.find_element(LoginPageLocators.BUTTON_AGREEMENTS_AND_POLICIES)
        ActionChains(self.driver).move_to_element(BUTTON_MORE).click(BUTTON_AGREEMENTS_AND_POLICIES).perform()