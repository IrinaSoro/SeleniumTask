from selenium.webdriver.common.by import By


class DropdownPageLocators:
    DROPDOWN_MENU_ONE = By.CSS_SELECTOR, 'select#dropdowm-menu-1'
    DROPDOWN_MENU_TWO = By.CSS_SELECTOR, 'select#dropdowm-menu-2'
    DROPDOWN_MENU_THREE = By.CSS_SELECTOR, 'select#dropdowm-menu-3'
    TOTAL_DROPDOWNS = (By.CSS_SELECTOR, '.section-title .dropdown-menu-lists')

class CheckboxPageLocators:
    CHECKBOX_OPTION_THREE = (By.XPATH, "//input[@value ='option-3']")
    CHECKBOX_OPTION_ONE = (By.XPATH, "//input[@value ='option-1']")


class RadioButtonsPageLocators:
    ORANGE_VALUE_OPTION = By.XPATH, "//option[@value='orange']"
    YELLOW_VALUE_OPTION = (By.XPATH, "//input[@value='yellow']")
    GABBAGE_VALUE_OPTION = (By.XPATH, "//input[@value='cabbage']")
    FRUITS_ITEMS = By.CSS_SELECTOR, "select#fruit-selects"