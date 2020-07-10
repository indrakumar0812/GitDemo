import pytest

@pytest.mark.skip
def test_firstprogram():
    msg = "hello"
    assert msg == "hi" , "Test failed coz string compare failed"

@pytest.mark.smoke
def test_secondPrg():
    a=4
    b=5
    assert a+2 == 6, "Assert don't match"

