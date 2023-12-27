from tests.BaseTest import browser
from tests.BaseTest import open_base_url
from pages.AgreementsAndPoliciesPage import AgreementsAndPoliciesHelper
from pages.LoginPage import LoginPageHelper
import allure

@allure.suite('Проверка перехода на страницы из списка,при нажатии на кнопку "еще"')
@allure.title('Отображение страницы Соглашения и политики')
def test_agreements_and_policies(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.clicButtonMoreSelectAgreementsAndPolicies()
    AgreementsAndPoliciesHelper(browser)