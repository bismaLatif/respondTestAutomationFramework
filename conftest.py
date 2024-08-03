import pytest
from selenium import webdriver
from utils.config import load_json
from api.api_client import APIClient

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login_data():
    return load_json('data/login_data.json')

@pytest.fixture(scope="module")
def api_endpoints():
    return load_json('data/api_endpoints.json')

@pytest.fixture(scope="module")
def api_client(api_endpoints):
    return APIClient(api_endpoints["base_url"])
