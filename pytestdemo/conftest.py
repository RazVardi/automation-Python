import pytest


@pytest.fixture(scope="function")
def setup():
    print("i will be be executing first")
    yield print("end")

@pytest.fixture()
def data_load():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


@pytest.yield_fixture(scope="function")
def destroy():
    print("i will be be executing after class")

@pytest.fixture(params=[("Chrome","Rahul","shetty"),("Firefox","Rahul"),"IE"])
def cross_browser(request):
    return request.param

