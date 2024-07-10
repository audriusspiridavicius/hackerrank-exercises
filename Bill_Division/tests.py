import pytest
from Bill_Division.main import bonAppetit



@pytest.mark.parametrize("bill,k,b", [
    ([3, 10, 2, 9], 3, 7.5),
    ([1,2,3,4,5,6,7], 4, 11.5),
    ([1,2,3,4,5,6,7], 6, 10.5),
    ([1,2], 0, 1),
    ([1,2], 1, 0.5),
    ])
def test_equals_to_bonAppetit(bill, k, b):
    expected_result = "Bon Appetit"
    assert bonAppetit(bill, k, b) == expected_result
  
    
@pytest.mark.parametrize("bill,k,b", [
    ([3, 10, 2, 9], 3, 7),
    ([1,2,3,4,5,6,7], 4, 11),
    ([1,2,3,4,5,6,7], 6, 10),
    ([1,2], 0, 3),
    ([1,2], 1, 3),
    ])
def test_not_equals_to_bonAppetit(bill, k, b):
    expected_result = "Bon Appetit"
    assert bonAppetit(bill, k, b) != expected_result


@pytest.mark.parametrize("bill,k,b,expected_result", [
    ([3, 10, 2, 9], 0, 15, 4.5),
    ([1,2,3], 1, 10, 8),
    ([1,2,3,4], 3, 10, 7),
    ([1,2], 0, 3, 2),
    ([1,2], 1, 3, 2.5),
    ])
def test_bonAppetit_bill_difference(bill, k, b, expected_result):

    assert bonAppetit(bill, k, b) == expected_result