import pytest

@pytest.mark.skip
def test_firstpgm():
    print("hello")

@pytest.mark.smoke
def test_Pgm():
    print("hi gm")
