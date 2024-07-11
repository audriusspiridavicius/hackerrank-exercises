import pytest
from functions import remove_spaces, get_grid_dimensions, text_to_grid, get_encrypted_text


@pytest.fixture
def text():
    return "good morning"

@pytest.fixture
def no_space_text(text):
    return remove_spaces(text)


@pytest.fixture
def size(no_space_text):
    return get_grid_dimensions(len(no_space_text))

@pytest.fixture
def text_grid(no_space_text, size):
    print(f"size = {size}")
    return text_to_grid(no_space_text, size[0], size[1])



@pytest.mark.parametrize("text,expected",[("good morning","goodmorning"), (" 1 2 3 4 5 6 7 9 ","12345679")])
def test_spaces_removed(text, expected):
    assert remove_spaces(text) == expected
    
    
@pytest.mark.parametrize("text_length,expected",[(30,(5,6)), (9,(3,3))])
def test_grid_dimensions_correct(text_length, expected):
    assert get_grid_dimensions(text_length) == expected
    
@pytest.mark.parametrize("text,rows,columns,expected",[
    ("goodmorning",3,4,[["g","o","o","d"],["m", "o", "r", "n"], ["i", "n", "g"]]),
    ("chillout",2,3,[["c","h","i"], ["l","l","o"], ["u","t"]])
    ])
def test_correct_grid_formed(text, rows, columns, expected):
    print(f"text_to_grid = {text_to_grid(text, rows, columns)}")
    assert text_to_grid(text, rows, columns) == expected
    


def test_get_encrypted_text(text_grid):
    encrypted_text = get_encrypted_text(text_grid)
    expected_enc_text = "gmi oon org dn"
    assert encrypted_text == expected_enc_text