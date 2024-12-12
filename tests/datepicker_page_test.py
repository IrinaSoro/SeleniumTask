import allure
from pages.datepicker_page import DatepickerPage

@allure.suite('Date picker')
class TestDatepickerPage:

    @allure.title('11 - Check date selection')
    def test_select_date(self, driver):
        datepicker_page = DatepickerPage(driver, "https://webdriveruniversity.com/Datepicker/index.html")
        datepicker_page.open()
        date1, cur_date, set_date = datepicker_page.select_date()
        print(date1, cur_date, set_date)