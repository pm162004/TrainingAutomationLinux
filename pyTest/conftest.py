import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":


        driver = webdriver.Chrome()
    elif browser == "edge":

        driver = webdriver.Edge()
    elif browser == "firefox":

        driver = webdriver.Firefox()
    return driver

def pytest_addoption(parser):    # This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):       # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# customizing reHTML Report
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Orange HRM'
    config._metadata['Module Name'] = 'Login Module'
    config._metadata['Tester Name'] = 'priya'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)