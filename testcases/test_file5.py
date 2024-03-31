import pytest


class Test:
    @pytest.mark.group1
    # @pytest.mark.skip
    def test_mul_0(self):
        x=5
        y=6
        mul=x*y
        if mul ==30:
            assert True
        else:
            assert False

##pytest =v to run all in more detail
##pytest -m (markarname)--> to run specific group test case





