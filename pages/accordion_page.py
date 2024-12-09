import allure

from locators.accordion_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
  locators = AccordianPageLocators()

  @allure.step('Select accordion and get the text shown')
  def check_accordian(self):
    self.wait_text_to_appear(self.locators.LOADING_COMPLETE_LABEL, 'LOADING COMPLETE.')
    label_text = self.element_is_present(self.locators.LOADING_COMPLETE_LABEL).text
    self.element_is_visible(self.locators.KEEP_CLICKING_BUTTON).click()
    appeared_text = self.element_is_visible(self.locators.APPEARED_TEXT).text
    self.element_is_visible(self.locators.KEEP_CLICKING_BUTTON).click()
    return label_text, appeared_text