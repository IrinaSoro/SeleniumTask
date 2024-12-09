import time
import allure

from locators.scroll_page_locators import ScrollPageLocators
from pages.base_page import BasePage


class ScrollPage(BasePage):
  locators = ScrollPageLocators()

  @allure.step('Scroll to zone 1')
  def scroll_to_elements(self):
      self.element_is_visible(self.locators.ZONE_ONE)
      time.sleep(2)
      zone1 = self.element_is_clickable(self.locators.ZONE_ONE)
      # self.action_move_to_element_and_click(zone1)
      self.scroll_to_element_by_coordinates(750, 150)
      zone1.click()
      time.sleep(2)
      text_zone1 = zone1.text
      with allure.step('Scroll to zone 2'):
          zone2 = self.element_is_visible(self.locators.ZONE_TWO)
          self.action_move_to_element_and_click(zone2)
          text_zone2 = zone2.text
          with allure.step('Scroll to zone 4'):
              self.scroll_to_element_by_coordinates(750,820)
              zone4 = self.element_is_visible(self.locators.ZONE_FOUR)
              zone4.click()
              text_zone4 = zone4.text
      return text_zone1, text_zone2, text_zone4