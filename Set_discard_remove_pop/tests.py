import unittest
from main import get_elements, get_operations
from unittest.mock import patch
class TestGetElements(unittest.TestCase):
    
    @patch("builtins.input", side_effect=['9','1 2 3 4 5 6 7 8 9'])
    def test_get_elements(self,*args):
        
        elemnts_number, elements = get_elements()

        self.assertEqual(9,elemnts_number)
        self.assertEqual(9,len(elements))

    @patch("builtins.input", side_effect=['9','1 2 3 4 5 6 7 8 9','3','pop','remove 9','discard 9'])
    def test_get_operations_result(self,*args):
        
        elemnts_number, elements = get_elements()
        
        operations = get_operations()
        
        self.assertEqual(3,len(operations))
        
    @patch("builtins.input", side_effect=['9','1 2 3 4 5 6 7 8 9','3','pop','remove 9','discard 9'])
    def test_get_operations_list_dict(self,*args):
        
        elemnts_number, elements = get_elements()
        
        operations = get_operations()
        
        self.assertIsInstance(operations,list)
        self.assertIsInstance(operations[0],dict)
        self.assertEqual("pop",operations[0]["operation"])
        self.assertEqual(None,operations[0]["value"])

if __name__ == "__main__":
    unittest.main()