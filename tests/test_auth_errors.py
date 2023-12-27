from tests.BaseTest import browser
from pages.LoginPage import LoginPageHelper
import allure
from random import randrange
from tests.BaseTest import open_base_url
from pages.RegistrationPage import RegistrationPageHelper

URL = "https://ok.ru"
LOGIN = randrange(25432689,868966543456788)
PASSWORD = randrange(15432689,768966543456788)
EMPTY_FORM_ERROR ="Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"
WRONG_PASSWORD_ERROR = "Неправильно указан логин и/или пароль"
REGISTRATION_EMPTY_PHONE_FIELD = "Неправильный номер телефона."

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка пустой формы авторизации')
def test_empty_auth_form(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.cliclLoginBatton()
    assert login_page_helper.getErrorText() == EMPTY_FORM_ERROR

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка пустого поля пароль')
def test_empty_password(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.set_login(LOGIN)
    login_page_helper.cliclLoginBatton()
    assert login_page_helper.getErrorText() == EMPTY_PASSWORD_ERROR

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка некорректного пароля')
def test_incorrect_password(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.set_login(LOGIN)
    login_page_helper.set_password(PASSWORD)
    login_page_helper.cliclLoginBatton()
    assert login_page_helper.getErrorText() == WRONG_PASSWORD_ERROR

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка регистрации на платформе без ввода телефонного номера')
def test_registration_empty_phone_field(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.clicRegistrationButton()
    registration_page_helper = RegistrationPageHelper(browser)
    registration_page_helper.click_further_button()
    assert registration_page_helper.getTextError() == REGISTRATION_EMPTY_PHONE_FIELD