import time
import allure
from locators.actions_page_locators import ActionsPageLocators
from pages.base_page import BasePage


class ActionsPage(BasePage):
  locators = ActionsPageLocators()

  @allure.step('Drag and drop the element')
  def drop_element(self):
      drag_div = self.element_is_visible(self.locators.DRAG_ME)
      drop_div = self.element_is_visible(self.locators.DROP_HERE)
      self.action_drag_and_drop_to_element(drag_div, drop_div)
      return  drop_div.text

  @allure.step('Double click')
  def double_click_element(self):
      color = self.action_double_click(self.locators.DOUBLE_CLICK_BUTTON)
      return color

  @allure.step('Move to element and click it')
  def check_alert_by_link(self):
      element =  self.element_is_visible(self.locators.HOVER_OVER_SECOND_BUTTON)
      self.action_move_to_element(element)
      self.element_is_visible(self.locators.LINK).click()
      with allure.step('Get the alert text'):
        text_alert = self.handle_alert_window()
      return text_alert

  @allure.step('Click and hold')
  def check_click_and_hold(self):
      click_button = self.element_is_visible(self.locators.CLICK_AND_HOLD_BUTTON)
      self.action_move_to_element(click_button)
      self.click_and_hold_element(click_button)
      return click_button.text

