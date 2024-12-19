import allure
from pages.accordion_page import AccordianPage


@allure.suite('Accordian')
class TestAccordianPage:

    URL = "/Accordion/index.html"

    @allure.title('3 - Check accordian items')
    def test_accordian_items(self, driver):
        accordian_page = AccordianPage(driver, self.URL)
        label_text, appeared_text= accordian_page.get_accordian_text()
        assert label_text == 'LOADING COMPLETE.', 'Loading has not been completed'
        assert appeared_text == 'This text has appeared after 5 seconds!', 'Text has not appeared'