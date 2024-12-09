import time
import allure
import pages.login_page

@allure.suite('Login')
class TestLoginPage:

    @allure.title('Verify login functionality')
    def test_login_and_accept_alert(self, driver):
        login_page = pages.login_page.LoginPage(driver, "https://webdriveruniversity.com/Login-Portal/fail.html")
        login_page.open()
        time.sleep(6)
        text_alert = login_page.fill_login_form()
        # assert text_alert == 'validation failed' , 'Validation alert is not shown'