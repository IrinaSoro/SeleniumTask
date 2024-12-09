import time

import allure

from locators.alerts_page_locators import AlertsPageLocators
from pages.base_page import BasePage



class AlertsPage(BasePage):
  locators = AlertsPageLocators()

  @allure.step('Switch to javascript alert')
  def check_js_alert(self):
      self.element_is_visible(self.locators.JAVASCRIPT_ALERT_BUTTON).click()
      time.sleep(6)
      self.switch_to_alert_window()

  @allure.step('Switch to modal popup')
  def check_modal_popup(self):
      self.element_is_visible(self.locators.MODAL_POPUP_BUTTON).click()
      self.element_is_visible(self.locators.CLOSE_MODAL_POPUP_BUTTON).click()

  @allure.step('Switch to confirmation box')
  def check_dismiss_confirm_box(self):
      self.element_is_visible(self.locators.JAVASCRIPT_CONFIRM_BOX_BUTTON).click()
      alert_window = self.driver.switch_to.alert
      with allure.step('Dismiss the confirmation box'):
          alert_window.dismiss()
          text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
      return text_result

  @allure.step('Switch to confirmation box')
  def check_accept_confirm_box(self):
      self.element_is_visible(self.locators.JAVASCRIPT_CONFIRM_BOX_BUTTON).click()
      alert_window = self.driver.switch_to.alert
      with allure.step('Accept the confirmation box'):
       alert_window.accept()
