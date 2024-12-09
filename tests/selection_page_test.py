import allure
from pages.selection_page import DropdownPage, CheckboxPage, RadioButtonsPage

@allure.suite('Dropdown')
class TestDropdownPage:

    @allure.title('Select options from dropdown')
    def test_dropdown(self, driver):
        dropdown_page = DropdownPage(driver, "https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        dropdown_page.open()
        dropdown_page.select_options_from_dropdown()

@allure.suite('Checkbox')
class TestCheckboxPage:

    @allure.title('Select checkbox option')
    def test_checkbox_options(self, driver):
        checkbox_page = CheckboxPage(driver,"https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        checkbox_page.open()
        checkbox_page.select_checkbox_option()

@allure.suite('Radio buttons')
class TestRadioButtonsPage:

    @allure.title('Verify radio button options state')
    def test_radio_buttons_options(self, driver):
        radio_button_page = RadioButtonsPage(driver,"https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        radio_button_page.open()
        orange_button, gabbage_button = radio_button_page.check_radio_button_options()
        assert not orange_button.is_enabled(), '"Orange" option is enabled'
        assert not gabbage_button.is_enabled(), '"Gabbage" option is enabled'

    @allure.title('Select an option')
    def test_fruit_selection(self, driver):
        radio_button_page = RadioButtonsPage(driver, "https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        radio_button_page.open()
        radio_button_page.select_fruit_option()