import random
import time
from pydoc import locate
from random import choice

import allure
from requests import delete
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from locators.alerts_page_locators import AlertsPageLocators
from locators.todo_list_page_locators import TodoListPageLocators
from locators.upload_file_locator import UploadFilePageLocators
from pages.base_page import BasePage


class TodoListPage(BasePage):
  locators = TodoListPageLocators()

  @allure.step('Add new item to Todo list')
  def update_todo_list_items(self):
      input_field = self.element_is_visible(self.locators.ADD_NEW_TODO_FIELD)
      count = 2
      while count > 0:
          input_field.click()
          input_field.send_keys(f"Test todo task {count}")
          input_field.send_keys(Keys.ENTER)
          count -=1
      with allure.step('Select a random item from Todo list'):
          item_list = self.elements_are_visible(self.locators.TODO_LIST_ITEMS)
          random_item = random.choice(item_list)
          with allure.step('Delete the randomly selected item from Todo list'):
              self.action_move_to_element(random_item)
              self.action_move_to_element_by_offset(random_item, -150, 0)
              time.sleep(3)
              items_list = self.elements_are_visible(self.locators.TODO_LIST_ITEMS)
      return len(items_list)