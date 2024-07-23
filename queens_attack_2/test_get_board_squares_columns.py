import pytest
from .index import get_board_squares


class TestColumnUpNoObstacles:
    
    board_size = 5
    obstacles = []
    row_step = 1
    column_step = 0

    
    def test_queen_center(self):
        
        queen_position = (3, 3)
        expected_outcome = [(4, 3), (5, 3)]
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
    
    def test_queen_top(self):
        
        queen_position = (4, 3)
        expected_outcome = [(5, 3)]
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
        
    def test_queen_top_edge(self):
        
        queen_position = (5, 3)
        expected_outcome = []
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
        
    def test_queen_bottom(self):
        
        queen_position = (2, 3)
        expected_outcome = [(3, 3), (4, 3), (5, 3)]
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
        
    def test_queen_bottom_edge(self):
        
        queen_position = (1, 3)
        expected_outcome = [(2, 3), (3, 3), (4, 3), (5, 3)]
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
        
    def test_queen_bottom_left_corner(self):
        
        queen_position = (1, 1)
        expected_outcome = [(2, 1), (3, 1), (4, 1), (5, 1)]
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
        
    def test_queen_bottom_right_corner(self):
        
        queen_position = (1, 5)
        expected_outcome = [(2, 5), (3, 5), (4, 5), (5, 5)]
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
        
class TestColumnUpWithObstacles:
    
    board_size = 5
    row_step = 1
    column_step = 0

    @pytest.mark.parametrize("obstacles,expected",[([(4, 3)],[]), ([(5, 3)],[(4, 3)])])
    def test_queen_center(self, obstacles, expected):
        
        queen_position = (3, 3)
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
    
    @pytest.mark.parametrize("obstacles,expected",[([(5, 3)],[]),([(3,3)],[(5,3)]), ([(1,3)],[(5,3)]), ([(1, 3), (2, 3)], [(5, 3)])])
    def test_queen_top(self, obstacles, expected):
        
        queen_position = (4, 3)
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
        
    @pytest.mark.parametrize("obstacles,expected",[([(4, 3)],[]),([(3,3)],[]), ([(1,3)],[]), ([(1, 3), (2, 3)], [])])
    def test_queen_top_edge(self, obstacles, expected):
        
        queen_position = (5, 3)
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
    
    @pytest.mark.parametrize("obstacles,expected",[([(4, 3)],[(3, 3)]),
                                                   ([(3,3)],[]),
                                                   ([(1,3)],[(3, 3), (4, 3), (5, 3)]),
                                                   ([(1, 3), (3, 3)], [])])    
    def test_queen_bottom(self, obstacles, expected):
        
        queen_position = (2, 3)
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
    
    @pytest.mark.parametrize("obstacles,expected",[([(4, 3)],[(2, 3), (3, 3)]),([(3,3)],[(2,3)]), ([(5, 3)], [(2, 3), (3, 3), (4, 3)])])        
    def test_queen_bottom_edge(self, obstacles, expected):
        
        queen_position = (1, 3)
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
    
    @pytest.mark.parametrize("obstacles,expected",[([(4, 1)],[(2, 1), (3, 1)]),
                                                   ([(3,3)],[(2,1), (3, 1), (4, 1), (5, 1)]),
                                                   ([(5, 1)], [(2, 1), (3, 1), (4, 1)])])           
    def test_queen_bottom_left_corner(self, obstacles, expected):
        
        queen_position = (1, 1)

        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
    
    
    @pytest.mark.parametrize("obstacles,expected",[([(4, 5)],[(2, 5), (3, 5)]),
                                                   ([(3,5)],[(2,5)]),
                                                   ([(5, 5)], [(2, 5), (3, 5), (4, 5)])]) 
    def test_queen_bottom_right_corner(self, obstacles, expected):
        
        queen_position = (1, 5)

        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
        


class TestColumnDownNoObstacles:
    
    
    
    board_size = 5
    obstacles = []
    row_step = -1
    column_step = 0

    
    def test_queen_center(self):
        
        queen_position = (3, 3)
        expected_outcome = [(2, 3), (1, 3)]
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
    
    def test_queen_top(self):
        
        queen_position = (4, 3)
        expected_outcome = [(3, 3), (2,3), (1, 3)]
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
        
    def test_queen_top_edge(self):
        
        queen_position = (5, 3)
        expected_outcome = [(4,3), (3, 3), (2, 3), (1, 3)]
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
        
    def test_queen_bottom(self):
        
        queen_position = (2, 3)
        expected_outcome = [(1, 3)]
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
        
    def test_queen_bottom_edge(self):
        
        queen_position = (1, 3)
        expected_outcome = []
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
        
    def test_queen_bottom_left_corner(self):
        
        queen_position = (1, 1)
        expected_outcome = []
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
        
    def test_queen_bottom_right_corner(self):
        
        queen_position = (1, 5)
        expected_outcome = []
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, self.obstacles)
        
        assert board_squares == expected_outcome
        
class TestColumnDomwnWithObstacles:
    
    board_size = 5
    row_step = -1
    column_step = 0

    @pytest.mark.parametrize("obstacles,expected",[([(4, 3)],[(2, 3),(1,3)]), ([(1, 3)],[(2, 3)])])
    def test_queen_center(self, obstacles, expected):
        
        queen_position = (3, 3)
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
    
    @pytest.mark.parametrize("obstacles,expected",[([(5, 3)],[(3, 3), (2, 3), (1, 3)]),
                                                   ([(3,3)],[]),
                                                   ([(1,3)],[(3,3),(2,3) ]),
                                                   ([(1, 3), (2, 3)], [(3, 3)])])
    def test_queen_top(self, obstacles, expected):
        
        queen_position = (4, 3)
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
        
    @pytest.mark.parametrize("obstacles,expected",[([(4, 3)],[]),
                                                   ([(3,3)],[(4, 3)]),
                                                   ([(1,3)],[(4, 3), (3, 3), (2,3)]),
                                                   ([(1, 3), (2, 3)], [(4, 3), (3, 3)])])
    def test_queen_top_edge(self, obstacles, expected):
        
        queen_position = (5, 3)
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
    
    @pytest.mark.parametrize("obstacles,expected",[([(4, 3)],[(1, 3)]),
                                                   ([(3,3)],[(1,3)]),
                                                   ([(1,3)],[]),
                                                   ([(1, 3), (3, 3)], [])])    
    def test_queen_bottom(self, obstacles, expected):
        
        queen_position = (2, 3)
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
    
    @pytest.mark.parametrize("obstacles,expected",[([(4, 3)],[]),
                                                   ([(3,3)],[]),
                                                   ([(5, 3)], [])])        
    def test_queen_bottom_edge(self, obstacles, expected):
        
        queen_position = (1, 3)
        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
    
    @pytest.mark.parametrize("obstacles,expected",[([(4, 1)],[]),
                                                   ([(3,3)],[]),
                                                   ([(5, 1)], [])])           
    def test_queen_bottom_left_corner(self, obstacles, expected):
        
        queen_position = (1, 1)

        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
    
    
    @pytest.mark.parametrize("obstacles,expected",[([(4, 5)],[]),
                                                   ([(3,5)],[]),
                                                   ([(5, 5)], [])]) 
    def test_queen_bottom_right_corner(self, obstacles, expected):
        
        queen_position = (1, 5)

        board_squares = get_board_squares(queen_position, self.board_size, self.row_step, self.column_step, obstacles)
        
        assert board_squares == expected
        