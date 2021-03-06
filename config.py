"""全局配置文件"""


from os.path import dirname,abspath,join


import logging
# 项目路径
basedir=abspath(dirname(__file__))

print(basedir)
# 截图存放路径
printscreen_path=join(basedir,'printscreen')



#日志配置
# noinspection PyArgumentList
logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] %(funcName)s: %(message)s",
                    datefmt="%Y/%m/%d %H:%M:%S",
                    handlers=[
                        logging.StreamHandler(),#将日志输出到终端
                        logging.FileHandler(join(basedir,'log','log.txt'),encoding='utf-8')
                    ])

DB_CONFIG_DEV = {
    'host': '121.196.148.211',
    'port': 3306,
    'database': 'test',
    'user': 'root',
    'password': 'root'
}


LT_db_config={
    'host': '115.28.108.130',
    'port': 3306,
    'database': 'longtengserver',
    'user': 'test',
    'password': 'abc123456',
    'charset':'utf8'

}

