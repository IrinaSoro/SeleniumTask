import allure
from pages.alerts_page import AlertsPage

@allure.suite('Check alerts')
class TestAlertsPage:

    URL = "/Popup-Alerts/index.html"

    @allure.title('7 - Check javascript alert')
    def test_js_alert(self, driver):
        alerts_page = AlertsPage(driver, self.URL)
        alerts_page.check_js_alert()

    @allure.title('7 - Check modal popup')
    def test_modal_popup(self, driver):
        alerts_page = AlertsPage(driver, self.URL)
        alerts_page.check_modal_popup()

    @allure.title('7 - Dismiss confirmation box')
    def test_dismiss_alert(self, driver):
        alerts_page = AlertsPage(driver, self.URL)
        alert_text = alerts_page.check_dismiss_confirm_box()
        assert alert_text == 'You pressed Cancel!'

    @allure.title('7 - Accept confirmation box')
    def test_accept_confirm_box(self, driver):
        alerts_page = AlertsPage(driver, self.URL)
        alerts_page.check_accept_confirm_box()