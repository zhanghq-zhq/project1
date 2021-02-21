from config import logging
import pytest
from utils.data import get_sheet

@pytest.mark.p1
@pytest.mark.parametrize(
    "x",get_sheet(
        "E:\\project1\\data\\test_data.xls",
        "Sheet1"
    )
)
def test_jia(x):
    logging.info("zhanghq{}".format(x))
    a=int(x["data1"])+int(x["data2"])
    assert a==int(x["assert"])