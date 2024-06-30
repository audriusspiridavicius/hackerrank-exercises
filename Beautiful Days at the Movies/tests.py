from index import is_beautiful_day


def test_day_is_beautiful():
    
    day = 20
    k = 6
    
    assert is_beautiful_day(day, k) == True


def test_day_is_not_beautiful():
    
    day = 20
    k = 5
    
    assert is_beautiful_day(day, k) == False

def test_day_single_digit():
    
    day = 2
    k = 5
    assert is_beautiful_day(day, k) == True
    
def test_day_3_digit():
    
    day = 123
    k = 5
    
    assert is_beautiful_day(day, k) == False
