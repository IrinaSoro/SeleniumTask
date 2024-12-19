import allure

from locators.iframe_page_locators import IframePageLocators
from pages.base_page import BasePage


class IframePage(BasePage):
  locators = IframePageLocators()

  @allure.step('Switch to frame')
  def get_iframe_section_description(self):
      frame = self.element_is_present(self.locators.FRAME)
      self.driver.switch_to.frame(frame)
      with allure.step('Get the section description'):
          text = self.element_is_present(self.locators.WHO_ARE_WE_SECTION_DESCRIPTION).text
          with allure.step('Switch to default content and navigate'):
              self.driver.switch_to.default_content()
              self.element_is_visible(self.locators.NAVIGATION_TITLE).click()
      return text