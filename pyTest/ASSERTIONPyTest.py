import pytest
def test_assert():
    a=9
    b=0
    assert a==b,"Failed"
    print("Passed")

def test_2():
    a=9
    b=0
    assert a>b,"Failed"
    print("Passed")

def test_3():
    a="pri"
    b="priya"
    assert a.__eq__(b),"Failed"
    print("Passed")