from .index import form_related_astronauts,get_astronauts_by_countries, get_related_astronauts, journeyToMoon
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
    
def test_related_astronauts(astronauts_info):
    n, group_dict = astronauts_info
    groups = get_related_astronauts(0,group_dict)
    assert len(groups)==n

def test_single_astronaut_group(astronauts_info):
    n, group_dict = astronauts_info
    groups = get_related_astronauts(0,group_dict)
    assert len(groups)==n
    
    
def test_single_country(astronauts_info):
    n, group_dict = astronauts_info
    country_groups = get_astronauts_by_countries(n, group_dict)
    assert len(country_groups) == 1
    
    
def test_multiple_countries(multi_astronauts_info):
    n, group_dict = multi_astronauts_info
    country_groups = get_astronauts_by_countries(n, group_dict)
    assert len(country_groups) == 2
    
@pytest.mark.parametrize("n,astronauts,expected_result",[
    (5,[[0,1],[2,3],[0,4]],6),
    (4,[[0,2]],5),
    (2,[[0,1]],0)])   
def test_journeyToMoon(n, astronauts, expected_result):
    
    result = journeyToMoon(n, astronauts)
    
    assert result == expected_result