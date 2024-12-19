import time
import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import UnexpectedAlertPresentException


class LoginPage(BasePage):
  locators = LoginPageLocators()

  @allure.step('Submit login form')
  def get_login_validation_alert_text(self):
      self.element_is_visible(self.locators.EMAIL).send_keys("Admin")
      self.element_is_visible(self.locators.PASSWORD).send_keys("Admin")
      self.element_is_visible(self.locators.SUBMIT).click()
      alert_text = self.handle_alert_window()
      return alert_text