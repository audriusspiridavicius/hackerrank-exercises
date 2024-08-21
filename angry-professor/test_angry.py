import pytest
from index import angryProfessor

class TestClassCancelled:
    
    @pytest.mark.parametrize("a", [([1, 2, 3]), ([]), ([10]),])
    def test_zero_attendees(self, a):
        k = 2
        class_cancelled = angryProfessor(k, a)
        assert class_cancelled == "YES"     
    
    @pytest.mark.parametrize("a", [([1, 2, 3. -1]), ([-1]), ([10, 0]), ([10, -1]) , ([1, 0]) , ([1, 0])])
    def test_one_attendee(self, a):
        k = 3
        class_cancelled = angryProfessor(k, a)
        assert class_cancelled == "YES"     
    
    @pytest.mark.parametrize("a", [([1, 2, -3. -1]), ([-1, 0]), ([-1, 10, 0]), ([0, 10, -1]) , ([-10, 1, 0]) , ([1, 0, -100])])
    def test_multiple_attendees(self, a):
        k = 3
        class_cancelled = angryProfessor(k, a)
        assert class_cancelled == "YES"
    
    



class TestClassNotCancelled:
    
    @pytest.mark.parametrize("a, k", [([1, 2, -3, -1], 2), ([-1,], 1), ([-1, 10, 0], 2), ([0, -10, -1], 3) , ([-10, -1, 0, -100], 4)])
    def test_on_time_students_equals_min_attendees(self, a, k):
        class_cancelled = angryProfessor(k, a)
        assert class_cancelled == "NO"
    
    @pytest.mark.parametrize("a, k", [([1, 2, -3, -1], 1), ([-1,], 0), ([-1, -10, 0], 2) , ([-10, -1, 0, -100], 3)])
    def test_on_time_students_greater_than_attendees(self, k, a):
        class_cancelled = angryProfessor(k, a)
        assert class_cancelled == "NO"