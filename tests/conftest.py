import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
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
def unique_email(request):
    base_email = 'testmail.*@fakemail.com.pl'
    unique_tag = f'test-{datetime.today().strftime("%d/%m/%y-%H.%M.%S")}'
    new_email = base_email.replace('*', unique_tag)
    request.cls.email = new_email
