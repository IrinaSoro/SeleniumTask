import allure

from locators.loader_page_locators import LoaderPageLocators
from pages.base_page import BasePage


class LoaderPage(BasePage):
  locators = LoaderPageLocators()

  @allure.step('Get alert title')
  def get_alert_title(self):
      self.element_is_disappear(self.locators.LOADER)
      self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
      alert_title = self.element_is_visible(self.locators.ALERT_TITLE)
      return alert_title.text

