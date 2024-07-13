import pytest
from index import countingValleys

@pytest.fixture
def only_mountains():
    return "UUDDUUDDUDUUUDDD"

@pytest.fixture
def only_valleys():
    return "DDUUDUDU"


def test_has_no_valleys(only_mountains):
    
    assert countingValleys(only_mountains) == 0

def test_has_valleys(only_valleys):
    
    assert countingValleys(only_valleys) > 0