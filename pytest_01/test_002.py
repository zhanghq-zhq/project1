import pytest


class Test_zhq():

    @pytest.mark.run(order=2)
    def test_001(self):
        print("001")
    @pytest.mark.skip
    @pytest.mark.run(order=1)
    def test_002(self):
        print("002")