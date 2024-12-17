import allure
from pages.datepicker_page import DatepickerPage

@allure.suite('Date picker')
class TestDatepickerPage:

    URL = "/Datepicker/index.html"

    @allure.title('11 - Check date selection')
    def test_select_date(self, driver):
        datepicker_page = DatepickerPage(driver, self.URL)
        default_date, current_date, set_date = datepicker_page.select_date()
        assert default_date == current_date, "Default date is not the current date"
        assert set_date == '01-01-2024', "The date has not been updated"
