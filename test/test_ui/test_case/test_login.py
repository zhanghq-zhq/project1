from test.test_ui.beaspage.szy_login_page import Login_page
from test.test_ui.beaspage.method_page import Goods_Method_Page
import pytest



@pytest.mark.parametrize('x',[{"name":"admin","pwd":"longtest123456"}])
def test_login_01(driver,x):
    if x.get('name')!='admin':
        pytest.skip("用户名错误，跳过测试，{}".format(x))

    Login_page(driver).login_method(x["name"],x["pwd"])
    Goods_Method_Page(driver).click_check_goods_list_method()