import os
import time
import allure
from generator.generator import generated_file
from locators.upload_file_locator import UploadFilePageLocators
from pages.base_page import BasePage



class UploadFilePage(BasePage):
  locators = UploadFilePageLocators()

  @allure.step('Generate a file to upload')
  def upload_file(self):
      path = generated_file()
      with allure.step('Upload the generated file'):
          self.element_is_visible(self.locators.INPUT_FILE_FIELD).send_keys(path)
          os.remove(path)
          self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
          is_alert_present = self.handle_alert_window()
          if is_alert_present is not None:
              return True
          else:
              print("Alert is not shown")
