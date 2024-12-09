import time

import allure
from requests import options
from selenium.webdriver.support.ui import Select

from locators.accordion_page_locators import AccordianPageLocators
from locators.selection_page_locators import DropdownPageLocators, CheckboxPageLocators, RadioButtonsPageLocators
from pages.base_page import BasePage
from tests.conftest import driver


class DropdownPage(BasePage):
  locators = DropdownPageLocators()

  @allure.step('Select options from the dropdowns')
  def select_options_from_dropdown(self):
      self.update_page_element_by_value(self.locators.DROPDOWN_MENU_ONE, 'c#')
      self.update_page_element_by_value(self.locators.DROPDOWN_MENU_TWO, 'maven')
      self.update_page_element_by_value(self.locators.DROPDOWN_MENU_THREE, 'css')



class CheckboxPage(BasePage):
  locators = CheckboxPageLocators()

  @allure.step('Select checkbox options')
  def select_checkbox_option(self):
        self.element_is_visible(self.locators.CHECKBOX_OPTION_THREE).click()
        self.element_is_visible(self.locators.CHECKBOX_OPTION_ONE).click()


class RadioButtonsPage(BasePage):
  locators = RadioButtonsPageLocators()

  @allure.step('Select radio button options')
  def check_radio_button_options(self):
        self.element_is_visible(self.locators.YELLOW_VALUE_OPTION).click()
        orange_button = self.element_is_visible(self.locators.ORANGE_VALUE_OPTION)
        gabbage_button =self.element_is_visible(self.locators.GABBAGE_VALUE_OPTION)
        return orange_button, gabbage_button

  @allure.step('Select a value from dropdown')
  def select_fruit_option(self):
      self.update_page_element_by_value(self.locators.FRUITS_ITEMS, 'apple')