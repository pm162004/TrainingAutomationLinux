import pytest
class TestClass:
    @pytest.fixture()
    def setup(self):
        global driver
        from selenium import webdriver
        print("Launching Browser")
        print("Open Application")
        yield
        print("Closing Browser")
    def test_login(self,setup):
        print("This is Login Test")
    def test_search(self,setup):
        print("This is Search Test")
    def test_advancedSearch(self,setup):
        print("This is Advanced Search Test")