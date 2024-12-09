from selenium.webdriver.common.by import By


class LoaderPageLocators:
    LOADER = (By.CSS_SELECTOR, 'div#loader')
    CLICK_ME_BUTTON = (By.CSS_SELECTOR, 'span#button1')
    ALERT_TITLE = (By.XPATH, "//h4[@class = 'modal-title']")
