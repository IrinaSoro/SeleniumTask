import time
from datetime import datetime
import allure

from locators.datepicker_page_locators import DatepickerPageLocators
from pages.base_page import BasePage



class DatepickerPage(BasePage):
  locators = DatepickerPageLocators()

  @allure.step('Select a new date')
  def select_date(self):
        date = self.element_is_visible(self.locators.DATE_PICKER)
        default_date = date.get_property("value")
        now = datetime.now()
        current_date = now.strftime("%m-%d-%Y")
        self.element_is_visible(self.locators.DATE_PICKER).click()
        self.element_is_visible(self.locators.SELECT_MONTH).click()
        self.element_is_visible(self.locators.MONTH_TO_SELECT).click()
        self.element_is_visible(self.locators.DAY_TO_SELECT).click()
        set_date = date.get_property("value")
        return default_date , current_date, set_date