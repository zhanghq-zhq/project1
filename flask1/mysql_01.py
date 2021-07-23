import pymysql
from flask import Flask,render_template



app=Flask(__name__)
DB_CONFIG_test = {
    'host': 'localhost',
    'port': 3306,
    'database': 'flask_data',
    'user': 'root',
    'password': ''
}


class Dbbase():


	def __init__(self):
		self.conn=pymysql.connect(**DB_CONFIG_test)
		self.cur=self.conn.cursor()

	def execute(self, sql):
		self.cur.execute(sql)
		result = self.cur.fetchall()
		return result




@app.route("/index")
def huqu_data():
	a=Dbbase().execute("select * from  flask_name")
	list1=[]
	list3=[]
	list2=["id","name","age","dizi"]
	for x in a:
		list1.append(dict(zip(list2,x)))
	# for xx in list1:
	# 	list3.append({"id":xx["id"],"data":xx})
	# print(list1)
	# print(list3)
	print(list1)
	return render_template("mysql_name_data.html",name=list1)

if __name__ == '__main__':
	app.run()














