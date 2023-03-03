# any pytest file should start with test_ or end with  _test
# pytest method names should start with test
# any module name should start with pytest
# any code should be wrapped in method only
# Method name should have sense
# -k stand for method names execution , -s logs in out put -v stand for more info metadata
# you can run specific file with py.test <filename>- doesn't work for some unknown reason
# you can mark (tag) tests @pyest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_first_program1():
    msg = "hello world"
    assert msg == "hi", "Test failed because string don't match"


@pytest.mark.xfail
def test_ballance():
    a = 5
    b = 20
    c = 4
    print("test ballance")
    assert a*c == b, "The test failed because the equation does not satisfy the equation"
