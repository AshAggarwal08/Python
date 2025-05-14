# Any pytest file should start with test_ or end with _test
# pytest method names should always start with test
import pytest


@pytest.mark.skip #only this test would be skipped others would run
def test_firstProgram():
    print("Hello first program")



