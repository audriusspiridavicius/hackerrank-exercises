from main import get_happiness
import unittest


class test_get_happines(unittest.TestCase):
    
    def setUp(self) -> None:
        
        self.numbers_array = [1, 5, 3]
        self.likeable_numbers = [3,1]
        self.dis_likeable_numbers = [5,7]
        
        return super().setUp()
    

    def test_get_happiness_level_1(self):
        
        
        hapiness_level = get_happiness(self.numbers_array, self.likeable_numbers, self.dis_likeable_numbers)
        
        self.assertEqual(1,hapiness_level, "happines should be equal to 1")
        
        
    def test_get_happiness_no_dis_likeable_numbers(self):
        
        dis_likeable_numbers = []
        
        with self.assertRaises(ValueError, msg="should throw error, because dislaikable array numbers is empty"):
            hapiness_level = get_happiness(self.numbers_array, self.likeable_numbers, dis_likeable_numbers)
            
    def test_get_happiness_no_likeable_numbers(self):
        
        likeable_numbers = []
        
        with self.assertRaises(ValueError, msg="should throw error, because laikable array numbers is empty"):
            hapiness_level = get_happiness(self.numbers_array, likeable_numbers, self.dis_likeable_numbers)
        
    def test_get_happiness_no_numbers_list(self):
        
        numbers_array = []
        
        with self.assertRaises(ValueError, msg="should throw error, because numbers array is empty"):
            hapiness_level = get_happiness(numbers_array, self.likeable_numbers, self.dis_likeable_numbers)
    
    def test_get_happiness_likeable_number_reapeats(self):
        numbers_array = [1, 5, 3, 1, 3]

        happiness = get_happiness(numbers_array,self.likeable_numbers, self.dis_likeable_numbers)
        
        self.assertEqual(3,happiness)
        
            
if __name__ == "__main__":
    unittest.main()