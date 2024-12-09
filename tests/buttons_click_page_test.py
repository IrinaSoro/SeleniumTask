import allure
from pages.buttons_click_page import ButtonsClickPage

@allure.suite('Click buttons')
class TestButtonsClickPage:

    @allure.title('Check js and webdriver click')
    def test_click_elements(self, driver):
        buttons_click_page = ButtonsClickPage(driver, "https://webdriveruniversity.com/Click-Buttons/index.html")
        buttons_click_page.open()
        buttons_click_page.click_elements()