import allure
from pages.buttons_click_page import ButtonsClickPage

@allure.suite('Click buttons')
class TestButtonsClickPage:

    URL = "/Click-Buttons/index.html"

    @allure.title('12 - Check js and webdriver click')
    def test_click_elements(self, driver):
        buttons_click_page = ButtonsClickPage(driver, self.URL)
        buttons_click_page.click_web_elements()