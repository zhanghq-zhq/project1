import pymysql

class My_Db():
    db_config={
        "host":"121.196.148.211",
        "port":3306,
        "user":"root",
        "password":"yourpass",
        "database":"jing_dong",
        "charset":"utf8"
    }

    def __init__(self):
        self.cou=pymysql.connect(**self.db_config)
        self.cs=self.cou.cursor()


    def select_my(self):
        input1=input("请问你是想查什么数据，1是查看全部数据，2是查看有哪些品牌，3是查看有哪些商品:")
        if int(input1)==int(1):
            self.cs.execute("select * from goods")
            x=self.cs.fetchall() #取全部数据
            #x=self.cs.fetchone() #取一调数据
            print(x)
        elif input1==2:
            self.cs.execute("select * from goods_cates;")
            x = self.cs.fetchall()  # 取全部数据
            # x=self.cs.fetchone() #取一调数据
            print(x)
        elif input1==3:
            self.cs.execute("select * from goods_name;")
            x = self.cs.fetchall()  # 取全部数据
            # x=self.cs.fetchone() #取一调数据
            print(x)

        self.cs.close()
            # 关闭Connection对象
        self.cou.close()


if __name__ == '__main__':
    My_Db().select_my()