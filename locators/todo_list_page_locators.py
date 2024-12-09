from selenium.webdriver.common.by import By

class TodoListPageLocators:
    ADD_NEW_TODO_FIELD = (By.XPATH, "//input[@type='text']")
    TODO_LIST_ITEMS = (By.CSS_SELECTOR, 'ul > li')
    DELETE_BUTTON = (By.XPATH, "//i[@class='fa fa-trash']")