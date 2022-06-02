import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
from helpers import generate_unique_email_and_tag
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='class')
def browser_driver(request):
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.close()


@pytest.fixture(scope='class')
def set_email_and_tag_attribute(request):
    new_email, tag = generate_unique_email_and_tag()
    request.cls.email = new_email
    request.cls.tag = tag
