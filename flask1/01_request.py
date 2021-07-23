# coding:utf-8

from flask import request,Flask
from flask_cors import CORS

app=Flask(__name__)
CORS(app,supports_credentials=True)

# 接口 api

# ip：port/index?city-shenzhen 查询字符串 OusryString
@app.route("/index",methods=["GET","POST"])
def index():
	# request中包含了前段发送过来的所有请求数据
	# 通过request.form可以直接提取请求体中的表单格式数据，是一个字典对象
	name=request.form.get("name","张三")
	age=request.form.get("age")
	city=request.args.get("city")
	get_list=request.form.getlist("name")
	a=request.data
	print(a)
	return "index name={},age={},  city={} getlist={}".format(name,age,city,get_list)

if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5210",debug=True)