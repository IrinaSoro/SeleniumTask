import allure

from pages.accordion_page import AccordianPage
from pages.actions_page import ActionsPage

@allure.suite('Check actions')
class TestActionsPage:

    @allure.title('Check drag and drop functionality')
    def test_drop_element(self, driver):
        actions_page = ActionsPage(driver, "https://webdriveruniversity.com/Actions/index.html")
        actions_page.open()
        dropped_text = actions_page.drop_element()
        assert dropped_text == 'Dropped!', "The element has not been dropped"

    @allure.title('Check double click')
    def test_double_click(self, driver):
        actions_page = ActionsPage(driver, "https://webdriveruniversity.com/Actions/index.html")
        actions_page.open()
        color = actions_page.double_click_element()
        assert color != '#FEC42D' and color == '#93CB5A', "Background color has not been changed"

    @allure.title('Check alert by link')
    def test_alert_by_link(self, driver):
        actions_page = ActionsPage(driver, "https://webdriveruniversity.com/Actions/index.html")
        actions_page.open()
        actions_page.check_alert_by_link()
        # print(alert_text)

    @allure.title('Check click and hold')
    def test_click_and_hold_functionality(self, driver):
         actions_page = ActionsPage(driver, "https://webdriveruniversity.com/Actions/index.html")
         actions_page.open()
         click_and_hold_text = actions_page.check_click_and_hold()
         assert 'Well done' in click_and_hold_text, 'The element is not held'