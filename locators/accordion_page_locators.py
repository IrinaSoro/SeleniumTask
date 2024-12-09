from selenium.webdriver.common.by import By


class AccordianPageLocators:
    APPEARED_TEXT = (By.CSS_SELECTOR, "div#timeout")
    LOADING_COMPLETE_LABEL = (By.CSS_SELECTOR, 'div#text-appear-box p#hidden-text')
    KEEP_CLICKING_BUTTON = (By.CSS_SELECTOR, 'button#click-accordion')