from selenium.webdriver.common.by import By


class ContactUsPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@name ='first_name']")
    LAST_NAME = (By.XPATH, "//input[@name ='last_name']")
    EMAIL = (By.XPATH, "//input[@name ='email']")
    COMMENTS =(By.XPATH, "//textarea[@name ='message']")
    CONTACT_US_FIELDS_LIST = (By.CSS_SELECTOR, '.feedback-input')
    RESET_BUTTON = (By.XPATH, "//input[@type='reset']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'body')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'h1')