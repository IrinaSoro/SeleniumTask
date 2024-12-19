import time
import allure

from locators.buttons_click_page_locators import ButtonsClickPageLocators
from pages.base_page import BasePage


class ButtonsClickPage(BasePage):
  locators = ButtonsClickPageLocators()

  @allure.step('Webdriver click')
  def click_web_elements(self):
      self.element_is_visible(self.locators.WEB_ELEM_CLICK_BUTTON).click()
      self.element_is_visible(self.locators.CLOSE_BUTTON).click()
      time.sleep(2)
      with allure.step('JS click'):
          js_click_button = self.element_is_visible(self.locators.JS_CLICK_BUTTON)
          self.js_click_element(js_click_button)

