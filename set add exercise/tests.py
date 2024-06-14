import unittest
from main import get_unique_stamps


class TestUniqueStamps(unittest.TestCase):
    
    def test_unique_stamps_no_dublicate_values(self):
        
        stamps = ['UK','China','USA', 'France', 'New Zealand']
        
        unique_stamps = get_unique_stamps(stamps)
        self.assertEqual(len(stamps),len(unique_stamps))
        
    def test_get_unique_stamps_has_dublicate_values(self):
        
        stamps = ['USA','UK','China','USA', 'France', 'New Zealand', 'China', 'China', 'UK','France','France']
        
        unique_stamps = get_unique_stamps(stamps)
        self.assertEqual(5,len(unique_stamps))
        
    def test_get_unique_stamps_empty_stamps_list(self):
        
        stamps = []
        
        unique_stamps = get_unique_stamps(stamps)
        self.assertEqual(0,len(unique_stamps))
        
    def test_get_unique_stamps_same_value(self):
        
        stamps = ['USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA']
        
        unique_stamps = get_unique_stamps(stamps)
        self.assertEqual(1,len(unique_stamps))
if __name__ == "__main__":
    unittest.main()