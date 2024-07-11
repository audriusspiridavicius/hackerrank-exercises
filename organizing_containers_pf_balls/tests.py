import pytest
from organizing_containers_pf_balls.main import organizingContainers

@pytest.mark.parametrize("containers",[([[3, 2],[2, 3]]),([[1, 3, 1],
                                                           [2, 1, 2],
                                                           [2, 1, 2]])])
def test_possible(containers):
    
    assert organizingContainers(containers) == "Possible"

@pytest.mark.parametrize("containers",[([[1, 4],[2, 3]]),([[1, 3, 1],[2, 1, 2],[3, 3, 3]])])
def test_impossible(containers):
    
    assert organizingContainers(containers) == "Impossible"