import time
import allure
from selenium.common import UnexpectedAlertPresentException, NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class BasePage:
    
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.get(f"https://webdriveruniversity.com{self.url}")

    @allure.step('Find a visible element')    
    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step('Find visible elements')    
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    
    @allure.step('Find a present element')    
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    @allure.step('Find present elements')    
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    
    @allure.step('Find a not visible element')
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element(locator))
    
    @allure.step('Find a clickable element')
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    @allure.step('Go to a specified element')
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Scroll to element by coordinates')
    def scroll_to_element_by_coordinates(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y});")

    @allure.step('Click an element using javascript')
    def js_click_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)


    @allure.step('Wait text to appear')
    def wait_text_to_appear(self, locator, text, timeout=10):
        return wait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step('Select element by value')
    def update_page_element_by_value(self, locator, value):
        element = wait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        Select(element).select_by_value(value)

    @allure.step('Wait until the element disappear')
    def element_is_disappear(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Switch to alert and accept')
    def handle_alert_window(self, timeout=5):
        alert_window = self.driver.switch_to.alert
        with allure.step('Accept the confirmation box'):
            alert_text = alert_window.text
            alert_window.accept()
        return alert_text

    @allure.step('Double click')
    def action_double_click(self, element):
        element = wait(self.driver, 10).until(EC.visibility_of_element_located(element))
        action = ActionChains(self.driver)
        action.double_click(element).perform()
        with allure.step('Convert rgb to hex'):
            rgb = element.value_of_css_property('background-color')
            hex_color = Color.from_string(rgb).hex
        return hex_color.upper()

    @allure.step('Drag and drop')
    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    @allure.step('Mouse to element')
    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @allure.step('Move to element by offset')
    def action_move_to_element_by_offset(self, element, x, y):
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(element, x, y)
        action.click()
        action.perform()

    @allure.step('Move to element and click')
    def action_move_to_element_and_click(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.click()
        action.perform()

    @allure.step('Click and hold element')
    def click_and_hold_element(self, element):
        action = ActionChains(self.driver)
        action.click_and_hold(element)
        action.perform()
