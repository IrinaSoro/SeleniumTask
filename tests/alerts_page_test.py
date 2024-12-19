import allure
from pages.alerts_page import AlertsPage

@allure.suite('Check alerts')
class TestAlertsPage:

    URL = "/Popup-Alerts/index.html"

    @allure.title('7 - Check javascript alert')
    def test_js_alert(self, driver):
        alerts_page = AlertsPage(driver, self.URL)
        alerts_page.get_js_alert()

    @allure.title('7 - Check modal popup')
    def test_modal_popup(self, driver):
        alerts_page = AlertsPage(driver, self.URL)
        alerts_page.switch_to_modal_popup()

    @allure.title('7 - Dismiss confirmation box')
    def test_dismiss_confirmation_box(self, driver):
        alerts_page = AlertsPage(driver, self.URL)
        alert_text = alerts_page.get_dismissed_confirmation_box_text()
        assert alert_text == 'You pressed Cancel!'

    @allure.title('7 - Accept confirmation box')
    def test_accept_confirmation_box(self, driver):
        alerts_page = AlertsPage(driver, self.URL)
        alerts_page.accept_confirmation_box()