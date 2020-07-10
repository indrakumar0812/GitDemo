#In pytest every code has to be written inside the function
#the file name has to be saves as test_
#pytest method name should always start with test_
import pytest


@pytest.mark.smoke
def test_firstprogram(setup):
    print("hello")


@pytest.mark.xfail
def test_secondprogram():
    print("good morning")
