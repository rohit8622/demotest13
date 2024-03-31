import pytest

class Test_2:
    @pytest.mark.sanity
    def test_sum_2(self):

        a=3
        b=4
        sum = a + b
        if sum == 7:
            assert True               ##test case status--->pass
            # assert False

        else:
            assert False              ##test case status--->fail
            # assert True













