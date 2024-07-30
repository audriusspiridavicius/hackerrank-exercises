import pytest
from index import decentNumber


class TestDecentNumber:
    
    def test_n_1(self):
        assert decentNumber(1) == "-1"
    
    def test_n_zero(self):
        assert decentNumber(1) == "-1"
        
    @pytest.mark.parametrize("n,expected_decent_number", [(3, 555), (5, 33333), (11, 55555533333), (15, 555555555555555), (13, 5553333333333)])
    def test_decent_number_exists(self, n, expected_decent_number):
        assert decentNumber(n) == expected_decent_number