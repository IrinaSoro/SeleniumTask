from selenium.webdriver.common.by import By


class IframePageLocators:
    WHO_ARE_WE_SECTION_DESCRIPTION = (By.CSS_SELECTOR, 'div:nth-of-type(1) > .thumbnail > .caption > p')
    NAVIGATION_TITLE = (By.CSS_SELECTOR, 'a#nav-title')
    FRAME = (By.CSS_SELECTOR, 'iframe#frame')
