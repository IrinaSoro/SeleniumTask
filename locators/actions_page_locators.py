from selenium.webdriver.common.by import By


class ActionsPageLocators:
    #drag and drop
    DRAG_ME = (By.CSS_SELECTOR, "div#draggable")
    DROP_HERE = (By.CSS_SELECTOR, "div#droppable")

     #double click
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "div#double-click")

    #hover over the button
    HOVER_OVER_SECOND_BUTTON = (By.CSS_SELECTOR, "div:nth-of-type(2) > .dropbtn")
    LINK = (By.CSS_SELECTOR, "div:nth-of-type(2) > .dropdown-content > .list-alert")

    # click and hold
    CLICK_AND_HOLD_BUTTON = (By.CSS_SELECTOR, 'div#click-box')

