import pytest

#@pytest.fixture(scope="class")-->Fixture will run only once before initializing the class
# otherwise it will be applied in method level

@pytest.fixture()
def setup():
    print("I will be executed first")
    yield
    print("I will execute last")

@pytest.fixture()
def dataLoad():
    print("userprofile data is being created")
    return ["Ram","kumar","rahulshettyacademy.com"]


@pytest.fixture(params=["chrome","firefox","IE"])
def crossBrowser(request):
   return request.param

#We can pass multiple parameters in tuple format also

#@pytest.fixture(params=[("chrome","Ram","Lord"),("firefox","kumar"),("IE","SS")])
#def crossBrowser(request):
#    return request.param
