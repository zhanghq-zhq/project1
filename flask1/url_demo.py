# coding:utf-8

from flask import Flask, current_app, redirect, url_for

app=Flask(__name__)

@app.route("/")
def index():
	"""定义视图函数"""
	return "hello flask"

# 通过methods绑定请求方式
@app.route("/post_only",methods=["GET","POST"])
def post_only():
	return "post only"



@app.route("/hello",methods=["POST"])
def hello():

	return "hello 1"



@app.route("/hello",methods=["GET"])
def hello2():

	return "hello 2"

@app.route("/hi1")
@app.route("/hi2")
def hi():
	return "hi agen"


@app.route("/login")
def login():

	# 使用url_for的函数，通过视图函数的名字找到视图对应的url路径
	url=url_for("index")
	return redirect(url)



if __name__ == '__main__':
	# 通过url_map可以查看整个flask中的路由
	print(app.url_map)
	app.run(host="0.0.0.0",port="5210",debug=True)