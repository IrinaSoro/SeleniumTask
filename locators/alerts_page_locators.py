from selenium.webdriver.common.by import By


class AlertsPageLocators:
    JAVASCRIPT_ALERT_BUTTON = (By.CSS_SELECTOR, 'span#button1')
    JAVASCRIPT_CONFIRM_BOX_BUTTON = (By.CSS_SELECTOR, 'span#button4')
    MODAL_POPUP_BUTTON = (By.CSS_SELECTOR, 'span#button2')
    CLOSE_MODAL_POPUP_BUTTON = (By.CSS_SELECTOR, '.modal-footer [data-dismiss]')
    CONFIRM_RESULT = (By.CSS_SELECTOR, 'p#confirm-alert-text')