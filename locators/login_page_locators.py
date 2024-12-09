from selenium.webdriver.common.by import By

class LoginPageLocators:
    
    EMAIL = (By.CSS_SELECTOR, 'input#text')
    PASSWORD = (By.CSS_SELECTOR, 'input#password')
    SUBMIT = (By.CSS_SELECTOR, 'button#login-button')