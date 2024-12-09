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
      file_name, path = generated_file()
      with allure.step('Upload the generated file'):
          self.element_is_visible(self.locators.INPUT_FILE_FIELD).send_keys(path)
          os.remove(path)
          self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
          time.sleep(3)
          is_alert_present = self.switch_to_alert_window()
      return is_alert_present
