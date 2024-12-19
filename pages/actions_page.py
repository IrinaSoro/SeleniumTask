import time
import allure
from locators.actions_page_locators import ActionsPageLocators
from pages.base_page import BasePage


class ActionsPage(BasePage):
  locators = ActionsPageLocators()

  @allure.step('Drag and drop the element')
  def get_dropped_text(self):
      drag_div = self.element_is_visible(self.locators.DRAG_ME)
      drop_div = self.element_is_visible(self.locators.DROP_HERE)
      self.action_drag_and_drop_to_element(drag_div, drop_div)
      return  drop_div.text

  @allure.step('Double click')
  def get_double_click_element_color(self):
      color = self.action_double_click(self.locators.DOUBLE_CLICK_BUTTON)
      return color

  @allure.step('Move to element and click it')
  def get_alert_by_link_text(self):
      element =  self.element_is_visible(self.locators.HOVER_OVER_SECOND_BUTTON)
      self.action_move_to_element(element)
      self.element_is_visible(self.locators.LINK).click()
      with allure.step('Get the alert text'):
        alert_text = self.handle_alert_window()
      return alert_text

  @allure.step('Click and hold')
  def get_click_and_hold_button_text(self):
      click_button = self.element_is_visible(self.locators.CLICK_AND_HOLD_BUTTON)
      self.action_move_to_element(click_button)
      self.click_and_hold_element(click_button)
      return click_button.text

