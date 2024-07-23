import pytest
from .index import get_board_squares

@pytest.fixture
def board_size():
    return 8

@pytest.fixture
def queens_position():
    
    return (4, 4)


@pytest.fixture
def no_obstacles():
    return [] 


@pytest.fixture
def row_step():
    return 0

@pytest.fixture
def column_step():
    return 1

class TestRowRightSquaresNoObstacles:
    
    def test_queen_middle(self, board_size, queens_position, no_obstacles, row_step, column_step):
        
        expected_result = [(4, 5), (4, 6), (4, 7), (4, 8)]
        
        board_squares = get_board_squares(queens_position, board_size, row_step, column_step, no_obstacles)
        
        assert board_squares == expected_result
        
    def test_queen_right(self, board_size, no_obstacles, row_step, column_step):
        
        queens_position = (4, 7)
        expected_result = [(4, 8)]
        
        board_squares = get_board_squares(queens_position, board_size, row_step, column_step, no_obstacles)
        
        assert board_squares == expected_result
        
    def test_queen_left(self, board_size, no_obstacles, row_step, column_step):
        
        queens_position = (4, 2)
        expected_result = [(4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)]
        
        board_squares = get_board_squares(queens_position, board_size, row_step, column_step, no_obstacles)
        
        assert board_squares == expected_result
        
    def test_queen_right_edge(self, board_size, no_obstacles, row_step, column_step):
        
        queens_position = (4, 8)
        expected_result = []
        
        board_squares = get_board_squares(queens_position, board_size, row_step, column_step, no_obstacles)
        
        assert board_squares == expected_result
        
    def test_queen_left_edge(self, board_size, no_obstacles, row_step, column_step):
        
        queens_position = (4, 1)
        expected_result = [(4, 2),(4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)]
        
        board_squares = get_board_squares(queens_position, board_size, row_step, column_step, no_obstacles)
        
        assert board_squares == expected_result 
    def test_queen_right_top_corner(self, board_size, no_obstacles, row_step, column_step):
        
        queens_position = (8, 8)
        expected_result = []
        
        board_squares = get_board_squares(queens_position, board_size, row_step, column_step, no_obstacles)
        
        assert board_squares == expected_result
        
    def test_queen_right_bottom_corner(self, board_size, no_obstacles, row_step, column_step):
        
        queens_position = (1, 8)
        expected_result = []
        
        board_squares = get_board_squares(queens_position, board_size, row_step, column_step, no_obstacles)
        
        assert board_squares == expected_result
        
        
class TestRowLeftSquaresNoObstacles:
    
    row_step = 0
    column_step = -1
    
    def test_queen_middle(self, board_size, queens_position, no_obstacles):
        
        expected_result = [(4, 3), (4, 2), (4, 1)]
        
        board_squares = get_board_squares(queens_position, board_size, self.row_step, self.column_step, no_obstacles)
        
        assert board_squares == expected_result
        
    def test_queen_right(self, board_size, no_obstacles):
        
        queens_position = (4, 7)
        expected_result = [(4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1)]
        
        board_squares = get_board_squares(queens_position, board_size, self.row_step, self.column_step, no_obstacles)
        
        assert board_squares == expected_result
        
    def test_queen_left(self, board_size, no_obstacles):
        
        queens_position = (4, 2)
        expected_result = [(4, 1)]
        
        board_squares = get_board_squares(queens_position, board_size, self.row_step, self.column_step, no_obstacles)
        
        assert board_squares == expected_result
        
    def test_queen_right_edge(self, board_size, no_obstacles):
        
        queens_position = (4, 8)
        expected_result = [(4, 7),(4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1)]
        
        board_squares = get_board_squares(queens_position, board_size, self.row_step, self.column_step, no_obstacles)
        
        assert board_squares == expected_result
        
    def test_queen_left_edge(self, board_size, no_obstacles):
        
        queens_position = (4, 1)
        expected_result = []
        
        board_squares = get_board_squares(queens_position, board_size, self.row_step, self.column_step, no_obstacles)
        
        assert board_squares == expected_result
         
    def test_queen_right_top_corner(self, board_size, no_obstacles):
        
        queens_position = (8, 8)
        expected_result = [(8, 7),(8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1)]
        
        board_squares = get_board_squares(queens_position, board_size, self.row_step, self.column_step, no_obstacles)
        
        assert board_squares == expected_result
    
    
    def test_queen_left_top_corner(self, board_size, no_obstacles):
        
        queens_position = (8, 1)
        expected_result = []
        
        board_squares = get_board_squares(queens_position, board_size, self.row_step, self.column_step, no_obstacles)
        
        assert board_squares == expected_result
        
    def test_queen_right_bottom_corner(self, board_size, no_obstacles):
        
        queens_position = (1, 8)
        expected_result = [(1, 7),(1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1)]
        
        board_squares = get_board_squares(queens_position, board_size, self.row_step, self.column_step, no_obstacles)
        
        assert board_squares == expected_result
        
    def test_queen_left_bottom_corner(self, board_size, no_obstacles):
        
        queens_position = (1, 1)
        expected_result = []
        
        board_squares = get_board_squares(queens_position, board_size, self.row_step, self.column_step, no_obstacles)
        
        assert board_squares == expected_result