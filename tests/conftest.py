from datetime import datetime

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='function')
def driver(request):
    global driver
    browser = request.config.getoption("browser")
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif browser == "edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome')

def browser(request):
    return request.config.getoption("--browser")