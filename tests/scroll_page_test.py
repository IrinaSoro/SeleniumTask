import allure
from pages.scroll_page import ScrollPage

@allure.suite('Scrolling')
class TestScrollPage:

    @allure.title('Verify scrolling to elements')
    def test_scroll_to_elements(self, driver):
        scroll_page = ScrollPage(driver, "https://webdriveruniversity.com/Scrolling/index.html")
        scroll_page.open()
        zone1_text, zone2_text, zone4_text = scroll_page.scroll_to_elements()
        assert zone1_text == 'Well done for scrolling to me!'
        assert zone2_text != 0
        assert zone4_text != 'Dont forget to scroll to me!'

