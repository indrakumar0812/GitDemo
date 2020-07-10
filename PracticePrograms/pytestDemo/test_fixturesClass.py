import pytest


@pytest.mark.usefixtures("setup")
class TestFixture:

    def test_fixtureDemo(self):
        print(" I will execute the fixture Demo method")

    def test_fixtureDemo1(self):
        print(" I will execute the fixture Demo1 method")

    def test_fixtureDemo2(self):
        print(" I will execute the fixture Demo2 method")

    def test_fixtureDemo3(self):
        print(" I will execute the fixture Demo3 method")