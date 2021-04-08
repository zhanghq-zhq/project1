import pymysql

from config import DB_CONFIG_DEV,LT_db_config


class DB_BASE():

    def __init__(self):
        self.conn=pymysql.connect(**LT_db_config)
        self.cur=self.conn.cursor()

    def select_hi(self,sql):
        """
        :param sql:
        :return:data
        """
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result


    def updata_db(self,sql):
        self.cur.execute(sql)
        self.conn.commit()

if __name__ == '__main__':
    a=DB_BASE().select_hi("select * from testuser;")
    print(a)