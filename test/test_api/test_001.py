import pytest
from test.test_api.data import DATA_JYK
from utils.db_base import DB_BASE
from config import logging


class Test_login():

    @pytest.mark.p1
    @pytest.mark.parametrize('x',DATA_JYK().data_add(1))
    def test_001(self,session,x):
        logging.info(f"测试添加加油卡，添加的数据是：{x}")
        DB_BASE().updata_db("delete from cardInfo where cardNumber='{}'".format(x['cardNumber']))
        url='http://115.28.108.130:8080/gasStation/process'
        data={
            "dataSourceId": "bHRz",
            "methodId": "00A",
            "CardInfo": {
                "cardNumber":f"{x['cardNumber']}"
            }
        }
        ru=session.post(url=url,json=data).json()
        select_db=DB_BASE().select_hi("select cardNumber from cardInfo where cardNumber='{}'".format(x['cardNumber']))
        assert select_db[0][0]==x['cardNumber']
        assert ru.get("code")==200
        assert ru.get("msg")=="添加卡成功"
        DB_BASE().updata_db("delete from cardInfo where cardNumber='{}'".format(x['cardNumber']))

