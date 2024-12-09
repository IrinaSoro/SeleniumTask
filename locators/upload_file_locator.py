from  selenium.webdriver.common.by import By

class UploadFilePageLocators:
    INPUT_FILE_FIELD = (By.CSS_SELECTOR, 'input#myFile')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input#submit-button')