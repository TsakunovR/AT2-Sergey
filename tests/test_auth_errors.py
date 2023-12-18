from tests.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
import allure
from random import randrange
from tests.BaseTest import open_base_url

URL = "https://ok.ru"
LOGIN = randrange(25432689,868966543456788)
PASSWORD = randrange(15432689,768966543456788)
EMPTY_FORM_ERROR ="Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"
WRONG_PASSWORD_ERROR = "Неправильно указан логин и/или пароль"

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










