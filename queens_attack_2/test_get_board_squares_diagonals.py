import pytest
from .index import get_board_squares


@pytest.fixture
def up_right_step():
    return 1, 1

@pytest.fixture
def up_left_step():
    return 1, -1

@pytest.fixture
def down_left_step():
    return -1, -1

@pytest.fixture
def down_right_step():
    return -1, 1

class TestQueenPositionCenter:
    
    board_size = 8
    queen_position = (4,4)
    
    @pytest.mark.parametrize("obstacles,expected_result",[
        ([], [(5, 5), (6, 6), (7, 7), (8, 8)]),
        ([(8, 8)], [(5, 5), (6, 6), (7, 7)]),
        ([(7, 7)], [(5, 5), (6, 6)]),
        ([(6, 6)], [(5, 5)]),
        ([(6, 6),(7, 7)], [(5, 5)]),
        ([(6, 6),(7, 7), (8, 8)], [(5, 5)]),
        ([(5, 5)], []),
    ])
    def test_diagonal_up_right(self, up_right_step, obstacles, expected_result):
        
        board_squares = get_board_squares(self.queen_position, self.board_size, row_step=up_right_step[0], column_step=up_right_step[1], obstacles=obstacles)
        assert board_squares == expected_result
    
        
    @pytest.mark.parametrize("obstacles,expected_result",[
        ([], [(5, 3), (6, 2), (7, 1)]),
        ([(5, 5)], [(5, 3), (6, 2), (7, 1)]),
        ([(3, 5)], [(5, 3), (6, 2), (7, 1)]),
        ([(3, 3)], [(5, 3), (6, 2), (7, 1)]),
        ([(8, 8)], [(5, 3), (6, 2), (7, 1)]),
        ([(1, 1)], [(5, 3), (6, 2), (7, 1)]),
        ([(7, 1)], [(5, 3), (6, 2)]),
        ([(6, 2)], [(5, 3)]),
        ([(5, 3)], []),
        
    ])
    def test_diagonal_up_left(self, up_left_step, obstacles, expected_result):
        
        board_squares = get_board_squares(self.queen_position, self.board_size, row_step=up_left_step[0], column_step=up_left_step[1], obstacles=obstacles)
        assert board_squares == expected_result
        
        
    @pytest.mark.parametrize("obstacles,expected_result",[
        ([], [(3, 3), (2, 2), (1, 1)]),
        ([(8,8)], [(3, 3), (2, 2), (1, 1)]),
        ([(7,8)], [(3, 3), (2, 2), (1, 1)]),
        ([(8,7)], [(3, 3), (2, 2), (1, 1)]),
        ([(8,1)], [(3, 3), (2, 2), (1, 1)]),
        ([(1,8)], [(3, 3), (2, 2), (1, 1)]),
        ([(1, 1)], [(3, 3), (2, 2)]),
        ([(2, 2)], [(3, 3)]),
        ([(3, 3)], []),
        ([(3, 3), (1,1)], []),
        ([(3, 3), (2,2)], []),
        ([(3, 3), (2, 2), (1, 1)], []),
    ])
    def test_diagonal_down_left(self, down_left_step, obstacles, expected_result):
        
        board_squares = get_board_squares(self.queen_position, self.board_size, row_step=down_left_step[0], column_step=down_left_step[1], obstacles=obstacles)
        assert board_squares == expected_result
        
        
    @pytest.mark.parametrize("obstacles,expected_result",[
        ([], [(3, 5), (2, 6), (1, 7)]),
        ([(8, 8)], [(3, 5), (2, 6), (1, 7)]),
        ([(1, 8)], [(3, 5), (2, 6), (1, 7)]),
        ([(8, 1)], [(3, 5), (2, 6), (1, 7)]),
        ([(5, 5)], [(3, 5), (2, 6), (1, 7)]),
        ([(5, 3)], [(3, 5), (2, 6), (1, 7)]),
        ([(3, 3)], [(3, 5), (2, 6), (1, 7)]),
        ([(1, 7)], [(3, 5), (2, 6)]),
        ([(2, 6)], [(3, 5)]),
        ([(3, 5)], []),
        ([(3, 5), (2, 6)], []),
        ([(3, 5), (2, 6), (1, 7)], []),


    ])
    def test_diagonal_down_right(self, down_right_step, obstacles, expected_result):
        
        board_squares = get_board_squares(self.queen_position, self.board_size, row_step=down_right_step[0], column_step=down_right_step[1], obstacles=obstacles)
        assert board_squares == expected_result