import pytest
from main import formingMagicSquare

class TestMagicSquareReturnValue:
    
    def test_returns_cost_7(self):
        s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
        
        cost = formingMagicSquare(s)
        
        assert cost == 7


