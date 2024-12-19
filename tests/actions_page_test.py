import allure
from pages.actions_page import ActionsPage

@allure.suite('Check actions')
class TestActionsPage:

    URL = "/Actions/index.html"

    @allure.title('6 - Check drag and drop functionality')
    def test_drag_and_drop_functionality(self, driver):
        actions_page = ActionsPage(driver, self.URL)
        dropped_text = actions_page.get_dropped_text()
        assert dropped_text == 'Dropped!', "The element has not been dropped"

    @allure.title('6 - Check double click')
    def test_double_click(self, driver):
        actions_page = ActionsPage(driver, self.URL)
        color = actions_page.get_double_click_element_color()
        assert color != '#FEC42D' and color == '#93CB5A', "Background color has not been changed"

    @allure.title('6 - Check alert by link')
    def test_alert_by_link(self, driver):
        actions_page = ActionsPage(driver, self.URL)
        alert_text = actions_page.get_alert_by_link_text()
        assert alert_text == 'Well done you clicked on the link!', 'Alert is not shown'

    @allure.title('6 - Check click and hold')
    def test_click_and_hold_functionality(self, driver):
         actions_page = ActionsPage(driver, self.URL)
         click_and_hold_text = actions_page.get_click_and_hold_button_text()
         assert 'Well done' in click_and_hold_text, 'The element is not held'