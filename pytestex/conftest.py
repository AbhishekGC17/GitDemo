import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print(" I will execute last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul",28,"rahulshettyacademy.com"]

@pytest.fixture(params=[("abhi","c","d"),"demo","jack"])
def Crossbrowser(request):
    return request.param

