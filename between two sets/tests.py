from index import getTotalX
import pytest


    
@pytest.fixture
def a_value():
    return [2, 4]

@pytest.fixture
def b_value():
    return [16, 32, 96]


def test_returns_3(a_value, b_value):
    assert getTotalX(a_value, b_value) == 3
    
def test_returns_2(a_value, b_value):
    
    a_value = [3, 4]
    b_value = [24, 48]
    
    assert getTotalX(a_value, b_value) == 2

