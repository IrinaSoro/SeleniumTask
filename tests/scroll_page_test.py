import allure
from pages.scroll_page import ScrollPage

@allure.suite('Scrolling')
class TestScrollPage:

    URL = "/Scrolling/index.html"

    @allure.title('13 - Verify scrolling to elements')
    def test_scroll_to_elements(self, driver):
        scroll_page = ScrollPage(driver, self.URL)
        zone1_text, zone2_text, zone4_text = scroll_page.scroll_to_elements()
        assert zone1_text == 'Well done for scrolling to me!', 'The element has not been scrolled'
        assert zone2_text != 0, 'The element has not been scrolled'
        assert zone4_text != 'Dont forget to scroll to me!', 'The element has not been scrolled'

