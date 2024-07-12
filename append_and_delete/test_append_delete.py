import pytest
from index import appendAndDelete


def test_s_string_empty():
    result = appendAndDelete("", "abc", 3)
    assert result == "Yes"

def test_t_string_empty():
    result = appendAndDelete("dfdsafdsaf", "", 1)
    assert result == "No"



@pytest.mark.parametrize("s,t,k",[("abc","123", 3), ("abc","123", 2), ("abc","123", 1), ("abc","123", 4), ("abc","123", 5), ("abc","ab30", 1), ("abc","ab30", 2)])
def test_prints_no(s, t, k):
    result = appendAndDelete(s, t, k)
    assert result == "No"
    
@pytest.mark.parametrize("s,t,k",[("abc","123", 6), ("abc","123", 7), ("abc","123", 8),
                                  ("abc","123", 9), ("abc","abc", 0), ("abc","ab30", 3)])
def test_prints_yes(s, t, k):
    result = appendAndDelete(s, t, k)
    assert result == "Yes"