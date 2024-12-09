from selenium.webdriver.common.by import By


class DatepickerPageLocators:
    DATE_PICKER = (By.XPATH, "//div[@id='datepicker']")
    # DATE_PICKER = (By.CSS_SELECTOR, 'input')
    SELECT_MONTH = (By.CSS_SELECTOR, '.datepicker-days .datepicker-switch')
    MONTH_TO_SELECT = (By.XPATH, "//span[text()='Jan']")
    DAY_TO_SELECT = (By.XPATH, "//td[text()='1' and @class='day']")