import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver