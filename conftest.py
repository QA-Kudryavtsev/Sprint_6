import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def base_url():
    return "https://qa-scooter.praktikum-services.ru/"

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()