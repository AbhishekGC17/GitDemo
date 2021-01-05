import pytest

@pytest.mark.xfail
def test_addition():
    a=2
    b=3
    print("addition:",a+b)
@pytest.mark.smoke
def test_subtraction():
    a=3
    b=4
    print("sub:",a-b)

def test_crossbrowser(Crossbrowser):
    print(Crossbrowser)