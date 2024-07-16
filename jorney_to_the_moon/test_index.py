from .index import form_related_astronauts
from collections import defaultdict
import pytest

@pytest.fixture
def astronauts_info():
    n=5
    test_data = [[0,2],[1,2],[2,3],[0,4]]
    group_dict = form_related_astronauts(test_data)
    return n, group_dict

@pytest.fixture
def multi_astronauts_info():
    n=5
    test_data = [[0,1],[2,3],[0,4]]
    group_dict = form_related_astronauts(test_data)
    return n, group_dict


def test_single_related_astronaut():
    test_data = [[0,2]]
    
    result:defaultdict = form_related_astronauts(test_data)
    
    assert result.get(0) == {2}
    assert result.get(2) == {0}
    
def test_multiple_related_astronauts():
    test_data = [[0,2],[0,3]]
    
    result:defaultdict = form_related_astronauts(test_data)
    
    assert result.get(0) == {2,3}
