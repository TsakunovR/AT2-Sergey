from tests.BaseTest import browser
from tests.BaseTest import open_base_url
from pages.AgreementsAndPoliciesPage import AgreementsAndPoliciesHelper
from pages.LoginPage import LoginPageHelper

def test_agreements_and_policies(browser, open_base_url):
    login_page_helper = LoginPageHelper(browser)
    login_page_helper.clicButtonMoreSelectAgreementsAndPolicies()
    AgreementsAndPoliciesHelper(browser)