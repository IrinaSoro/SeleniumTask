from selenium.webdriver.common.by import By


class ButtonsClickPageLocators:
    WEB_ELEM_CLICK_BUTTON = (By.XPATH, "//span[@id='button1']")
    JS_CLICK_BUTTON = (By.CSS_SELECTOR, 'span#button2')
    CLOSE_BUTTON = (By.XPATH, "//button[text()='Close']")