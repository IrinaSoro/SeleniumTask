import time

import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import UnexpectedAlertPresentException


class LoginPage(BasePage):
  locators = LoginPageLocators()

  @allure.step('Submit login form')
  def fill_login_form(self):
      self.element_is_visible(self.locators.EMAIL).send_keys("Admin")
      self.element_is_visible(self.locators.PASSWORD).send_keys("Admin")
      self.element_is_visible(self.locators.SUBMIT).click()
      time.sleep(5)
      with allure.step('Switch to alert and handle the possible error'):
          self.switch_to_alert_window()
