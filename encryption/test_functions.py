import pytest
from functions import remove_spaces, get_enceyption_step, get_encrypted_text


@pytest.fixture
def text():
    return "good morning"

@pytest.fixture
def no_space_text(text):
    return remove_spaces(text)


@pytest.fixture
def size(no_space_text):
    return get_enceyption_step(len(no_space_text))



@pytest.mark.parametrize("text,expected",[("good morning","goodmorning"), (" 1 2 3 4 5 6 7 9 ","12345679")])
def test_spaces_removed(text, expected):
    assert remove_spaces(text) == expected
    

@pytest.mark.parametrize("text,encrypted_text",[("goodmorning","gmi oon org dn"),("haveaniceday", "hae and via ecy")])
def test_text_encrypted_correctlly(text, encrypted_text):

    assert get_encrypted_text(text) == encrypted_text