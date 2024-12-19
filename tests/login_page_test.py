import time
import allure
import pytest

from pages.login_page import LoginPage

@allure.suite('Login')
class TestLoginPage:

    URL = "/Login-Portal/fail.html"

    @allure.title('1 - Verify login functionality')
    def test_login_and_accept_alert(self, driver):
        login_page = LoginPage(driver, self.URL)
        text_alert = login_page.get_login_validation_alert_text()
        assert text_alert == 'validation failed' , 'Validation alert is not shown'