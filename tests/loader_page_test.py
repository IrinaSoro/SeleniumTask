import allure
from pages.loader_page import LoaderPage

@allure.suite('Loader')
class TestLoaderPage:

    URL = "/Ajax-Loader/index.html"

    @allure.title('5 - Check alert after loader')
    def test_alert_title(self, driver):
        loader_page = LoaderPage(driver, self.URL)
        alert_text = loader_page.get_alert_title()
        assert 'Well Done' in alert_text, 'Alert title doesnt match'