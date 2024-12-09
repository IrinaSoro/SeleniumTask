import allure

from pages.alerts_page import AlertsPage

@allure.suite('Check alerts')
class TestAlertsPage:

    @allure.title('Check javascript alert')
    def test_js_alert(self, driver):
        alerts_page = AlertsPage(driver, "https://webdriveruniversity.com/Popup-Alerts/index.html")
        alerts_page.open()
        text = alerts_page.check_js_alert()
        print(text)

    @allure.title('Check modal popup')
    def test_modal_popup(self, driver):
        alerts_page = AlertsPage(driver, "https://webdriveruniversity.com/Popup-Alerts/index.html")
        alerts_page.open()
        alerts_page.check_modal_popup()

    @allure.title('Dismiss confirmation box')
    def test_dismiss_alert(self, driver):
        alerts_page = AlertsPage(driver, "https://webdriveruniversity.com/Popup-Alerts/index.html")
        alerts_page.open()
        alert_text = alerts_page.check_dismiss_confirm_box()
        assert alert_text == 'You pressed Cancel!'

    @allure.title('Accept confirmation box')
    def test_accept_confirm_box(self, driver):
        alerts_page = AlertsPage(driver, "https://webdriveruniversity.com/Popup-Alerts/index.html")
        alerts_page.open()
        alerts_page.check_accept_confirm_box()