import pytest
from climbing_the_leaderboard.main import climbing_leaderboard


@pytest.fixture
def leaderboard():
    return [100,100, 90, 90, 80, 75,75, 60]


def test_player_played_one_game(leaderboard):
    """Test that a player played one game."""
    
    position = climbing_leaderboard(leaderboard, [95])
    assert 2 == position[0] 

    
def test_player_played_multiple_games(leaderboard):

    position = climbing_leaderboard(leaderboard, [200,200])
    assert [1,1] == position
    
def test_player_played_zero_games(leaderboard):
    
    position = climbing_leaderboard(leaderboard, [])
    assert [] == position
    
def test_player_takes_first_place(leaderboard):
    
    position = climbing_leaderboard(leaderboard, [1000])
    assert 1 == position[0]

def test_player_takes_last_place(leaderboard):
    
    last_position = len(set(leaderboard)) + 1
    
    position = climbing_leaderboard(leaderboard, [1])
    assert last_position == position[0]

def test_player_takes_last_then_first_place(leaderboard):
    
    games = [1,10000]
    last_position = len(set(leaderboard)) + 1
    first_position = 1
    
    position = climbing_leaderboard(leaderboard, games)
    assert [last_position, first_position] == position

def test_non_existing_scores(leaderboard):
    
    
    games = [10, 61, 70]
    expected_result = [6, 5, 5]
    
    position = climbing_leaderboard(leaderboard, games)
    
    assert position == expected_result
    
def test_existing_scores(leaderboard):
    
    
    games = [100, 90, 80]
    expected_result = [1, 2, 3]
    
    position = climbing_leaderboard(leaderboard, games)
    
    assert position == expected_result  
    
