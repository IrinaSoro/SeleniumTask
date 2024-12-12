import allure
from pages.accordion_page import AccordianPage

@allure.suite('Accordian')
class TestAccordianPage:

    @allure.title('3 - Check accordian items')
    def test_accordian(self, driver):
        accordian_page = AccordianPage(driver, "https://webdriveruniversity.com/Accordion/index.html")
        accordian_page.open()
        label_text, appeared_text= accordian_page.check_accordian()
        assert label_text == 'LOADING COMPLETE.', 'Loading has not been completed'
        assert appeared_text == 'This text has appeared after 5 seconds!', 'Text has not appeared'