import pytest

@pytest.mark.smoke    #used to mark the ptests as smoke/ regression/unit etc so that only that group is run in terminal
def test_secondProgram():
    print("second program")