import pytest
from index import designerPdfViewer


#letters abcdefghij k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
#indexes 0123456789 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

@pytest.fixture
def letter_heights():
    letter_heights= [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 7]
    return letter_heights

@pytest.fixture
def letter_heights_same():
    letter_heights=[1 for _ in range(0,26)]
    return letter_heights


@pytest.fixture
def short_word():
    return "abc"

@pytest.fixture
def long_word():
    return "hellowworld"

@pytest.fixture
def word_same_letter():
    return "yyyyyyyyyy"

def test_short_word(letter_heights, short_word):
    
    assert designerPdfViewer(letter_heights, short_word) == 9

def test_long_word(letter_heights, long_word):
    
    assert designerPdfViewer(letter_heights, long_word) == 55

def test_word_same_letter_repeats(letter_heights, word_same_letter):
    
    assert designerPdfViewer(letter_heights, word_same_letter) == 100
    
def test_letter_height_all_same(letter_heights_same,word_same_letter):
    assert designerPdfViewer(letter_heights_same, word_same_letter) == len(word_same_letter)

def test_letter_height_all_same2(letter_heights_same,long_word):
    assert designerPdfViewer(letter_heights_same, long_word) == len(long_word)

def test_letter_height_all_same3(letter_heights_same,short_word):
    assert designerPdfViewer(letter_heights_same, short_word) == len(short_word)