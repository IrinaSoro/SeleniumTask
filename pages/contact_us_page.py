import time
import allure

from generator.generator import generated_person_data
from locators.contact_us_page_locators import ContactUsPageLocators
from pages.base_page import BasePage


class ContactUsPage(BasePage):
  locators = ContactUsPageLocators()

  @allure.step('Check placeholders in list items')
  def get_placeholders_list(self):
      item_list = self.elements_are_visible(self.locators.CONTACT_US_FIELDS_LIST)
      data = []
      for item in item_list:
          text_value = item.get_attribute("placeholder")
          data.append(text_value)
      return tuple(data)

  def get_required_fields_error_message(self):
      person_data = next(generated_person_data())
      self.element_is_visible(self.locators.FIRST_NAME).send_keys(person_data.firstname)
      self.element_is_visible(self.locators.LAST_NAME).send_keys(person_data.lastname)
      self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
      time.sleep(2)
      required_fields_error_message = self.element_is_visible(self.locators.ERROR_MESSAGE).text
      for text in required_fields_error_message.splitlines():
          return text.split(": ")

  @allure.step('Fill in form with invalid email')
  def get_incorrect_email_address_error_message(self):
      person = next(generated_person_data())
      self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
      self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
      self.element_is_visible(self.locators.EMAIL).send_keys(person.incorrect_email)
      self.element_is_visible(self.locators.COMMENTS).send_keys(person.comment)
      self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
      time.sleep(4)
      error_message_text = self.element_is_visible(self.locators.ERROR_MESSAGE).text
      return error_message_text.split(": ")

  @allure.step('Send comment')
  def get_successfully_sent_comment_message(self):
      person = next(generated_person_data())
      self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
      self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
      self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
      self.element_is_visible(self.locators.COMMENTS).send_keys(person.comment)
      self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
      time.sleep(4)
      current_url = self.driver.current_url
      with allure.step('Get the success message'):
       success_message = self.element_is_visible(self.locators.SUCCESS_MESSAGE).text
      return current_url, success_message

