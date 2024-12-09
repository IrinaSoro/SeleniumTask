import time
from itertools import permutations

import allure

from generator.generator import generated_person
from locators.contact_us_page_locators import ContactUsPageLocators
from pages.base_page import BasePage



class ContactUsPage(BasePage):
  locators = ContactUsPageLocators()

  @allure.step('Check placeholders in list items')
  def verify_placeholders(self):
      item_list = self.elements_are_visible(self.locators.CONTACT_US_FIELDS_LIST)
      data = []
      for item in item_list:
          text_value = item.get_attribute("placeholder")
          data.append(text_value)
      return tuple(data)

  @allure.step('Fill in form with invalid email')
  def verify_incorrect_email_address_error(self):
      person = next(generated_person())
      self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
      self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
      self.element_is_visible(self.locators.EMAIL).send_keys(person.incorrect_email)
      self.element_is_visible(self.locators.COMMENTS).send_keys(person.comment)
      self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
      time.sleep(4)
      error_text = self.element_is_visible(self.locators.ERROR_MESSAGE).text
      return error_text.split(": ")

  @allure.step('Send comment')
  def verify_successfully_sent_comment(self):
      person = next(generated_person())
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

