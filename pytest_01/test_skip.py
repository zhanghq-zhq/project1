import pytest




class Test_skip():

    @pytest.mark.skip("经过上轮测试，改用例有bug,在没有修复前跳过")
    def test_001(self):

        assert 1==1

    @pytest.mark.run(order=1)
    def test_002(self):

        a=1
        b=2
        if a!=b:
            pytest.skip("经过上轮测试，改用例有bug,在没有修复前跳过")
        assert a == b


    @pytest.mark.skipif(1==1,reason='测试条件不满住')
    def test_003(self):

        assert 1==1