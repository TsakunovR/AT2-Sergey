from tests.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.PasswordRecoveryPage import PasswordRecoveryPageHelper
from pages.AccessRecoveryPage import AccessRecoveryPageHelper
import allure
from random import randrange
from tests.BaseTest import open_base_url
from pages.RecoveryByPhonePage import RecoveryByPhonePageHelper
from pages.RecoveryByEmailPage import RecoveryByEmailPageHelper

URL ="https://ok.ru"
LOGIN = randrange(25432689,868966543456788)
#PASSWORD = randrange(15432689,768966543456788)
EMPTY_FIELD_EMAIL_ERROR = "Неправильный формат почты"

@allure.suite('Проверка формы восстановленя профиля')
@allure.title('Проверка перехода на страницу восстановления профиля')
def test_open_password_recovery_window(browser):
    base_page = BasePage(browser)
    base_page.go_to_url(URL)
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.set_login(LOGIN)
    for i in range (0,3):
        PASSWORD_RND = randrange(15432689, 7689665434788)
        login_page_helper.set_password(PASSWORD_RND)
        login_page_helper.cliclLoginBatton()
    PasswordRecoveryPageHelper(browser)

@allure.suite('Проверка формы восстановленя профиля')
@allure.title('Восстановление профиля по телефону')
def test_recovery_by_phone(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.clicCantSignIn()
    Access_Recovery_PageHelper = AccessRecoveryPageHelper(browser)
    Access_Recovery_PageHelper.clickPhoneButton()
    recovery_by_phone_page = RecoveryByPhonePageHelper(browser)
    RES_SELECT_COUNTRY = recovery_by_phone_page.select_country(5)
    RES_PHONE_CODE = recovery_by_phone_page.get_phone_code_from_field()
    assert RES_SELECT_COUNTRY == RES_PHONE_CODE

@allure.suite('Проверка формы восстановленя профиля')
@allure.title('Восстановление профиля по почте')
def test_recovery_by_email(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.clicCantSignIn()
    access_recovery_pageHelper = AccessRecoveryPageHelper(browser)
    access_recovery_pageHelper.clickEmailButton()
    recovery_by_email_page = RecoveryByEmailPageHelper(browser)
    recovery_by_email_page.cliclGetCodeButton()
    assert recovery_by_email_page.getTextError() == EMPTY_FIELD_EMAIL_ERROR