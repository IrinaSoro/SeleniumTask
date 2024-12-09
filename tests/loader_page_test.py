import allure
from pages.loader_page import LoaderPage

@allure.suite('Loader')
class TestLoaderPage:

    @allure.title('Check alert after loader')
    def test_alert_title(self, driver):
        loader_page = LoaderPage(driver, 'https://webdriveruniversity.com/Ajax-Loader/index.html')
        loader_page.open()
        alert_text = loader_page.get_alert_title()
        assert 'Well Done' in alert_text, 'Alert title doesnt match'