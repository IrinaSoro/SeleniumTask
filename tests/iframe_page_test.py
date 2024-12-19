import allure
from pages.iframe_page import IframePage

@allure.suite('Iframe')
class TestIframePage:

    URL = "/IFrame/index.html"

    @allure.title('8 - Check iframe section description')
    def test_iframe_section_description(self, driver):
        iframe_page = IframePage(driver, self.URL)
        section_description = iframe_page.get_iframe_section_description()
        assert 'Lorem ipsum' in section_description