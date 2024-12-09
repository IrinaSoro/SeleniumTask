import allure
from pages.iframe_page import IframePage

@allure.suite('Iframe')
class TestIframePage:

    @allure.title('Check iframe section description')
    def test_frame_section_description(self, driver):
        iframe_page = IframePage(driver, "https://webdriveruniversity.com/IFrame/index.html")
        iframe_page.open()
        section_description = iframe_page.check_section_description()
        assert 'Lorem ipsum' in section_description