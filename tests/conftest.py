from datetime import datetime
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='function')
def driver():
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    # driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()