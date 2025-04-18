import pytest


@pytest.mark.smoke
def test_one():
    print("Inside test_one")

@pytest.mark.regression
def test_two():
    print("Inside test_two")

@pytest.mark.regression
def test_three():
    print("Inside test_three")
