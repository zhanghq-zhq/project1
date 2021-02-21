import pymysql

from config import DB_CONFIG_DEV


class DB_BASE():

    def __init__(self):
        self.conn=pymysql.connect(**DB_CONFIG_DEV)
        self.cur=self.conn.cursor()

    def select_hi(self,sql):
        """
        :param sql:
        :return:data
        """
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result


if __name__ == '__main__':
    a=DB_BASE().select_hi("select * from testuser;")
    print(a)