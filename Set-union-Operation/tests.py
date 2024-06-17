import pytest
from main import get_subscibers_count

@pytest.fixture
def get_eng_french_subs():
    return [1, 2, 3], [1, 4, 5, 6, 7]

@pytest.fixture
def get_eng_only_subs():
    return [1, 2, 3], []

@pytest.fixture
def get_french_only_subs():
    return [], [1, 2, 3]

class TestGetSubscibersCount:
    
    
    def test_returns_unique_values(self,get_eng_french_subs):
        
        eng_subs, french_subs = get_eng_french_subs
        
        subs_count = get_subscibers_count(eng_subs, french_subs)
        
        assert subs_count == 7


    def test_subscribed_only_english(self, get_eng_only_subs):
        
        eng_subs, french_subs = get_eng_only_subs
        
        subs_count = get_subscibers_count(eng_subs, french_subs)
        
        assert subs_count == len(eng_subs)       

    def test_subscribed_only_french(self, get_french_only_subs):
        
        eng_subs, french_subs = get_french_only_subs
        
        subs_count = get_subscibers_count(eng_subs, french_subs)
        
        assert subs_count == len(french_subs)    
        assert subs_count != len(eng_subs)    

if __name__ == "__main__":
  
    retcode = pytest.main()