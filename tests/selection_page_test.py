import allure
from pages.selection_page import DropdownPage, CheckboxPage, RadioButtonsPage

@allure.suite('Dropdown')
class TestDropdownPage:

    URL = "/Dropdown-Checkboxes-RadioButtons/index.html"

    @allure.title('4 - Select options from dropdown')
    def test_dropdown(self, driver):
        dropdown_page = DropdownPage(driver, self.URL)
        dropdown_page.select_options_from_dropdown()

@allure.suite('Checkbox')
class TestCheckboxPage:

    URL = "/Dropdown-Checkboxes-RadioButtons/index.html"

    @allure.title('4 - Select checkbox option')
    def test_checkbox_options(self, driver):
        checkbox_page = CheckboxPage(driver,self.URL)
        checkbox_page.select_checkbox_option()

@allure.suite('Radio buttons')
class TestRadioButtonsPage:

    URL = "/Dropdown-Checkboxes-RadioButtons/index.html"

    @allure.title('4 - Verify radio button options state')
    def test_radio_buttons_options(self, driver):
        radio_button_page = RadioButtonsPage(driver,self.URL)
        orange_button, gabbage_button = radio_button_page.check_radio_button_options()
        assert not orange_button.is_enabled(), '"Orange" option is enabled'
        assert not gabbage_button.is_enabled(), '"Gabbage" option is enabled'

    @allure.title('4 - Select an option')
    def test_fruit_selection(self, driver):
        radio_button_page = RadioButtonsPage(driver, self.URL)
        radio_button_page.select_fruit_option()