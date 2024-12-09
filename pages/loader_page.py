import time

import allure
from requests import options
from selenium.webdriver.support.ui import Select

from locators.accordion_page_locators import AccordianPageLocators
from locators.loader_page_locators import LoaderPageLocators
from locators.selection_page_locators import DropdownPageLocators, CheckboxPageLocators, RadioButtonsPageLocators
from pages.base_page import BasePage
from tests.conftest import driver


class LoaderPage(BasePage):
  locators = LoaderPageLocators()

  @allure.step('Get alert title')
  def get_alert_title(self):
      self.element_is_disappear(self.locators.LOADER)
      self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
      alert_title = self.element_is_visible(self.locators.ALERT_TITLE)
      return alert_title.text

