# coding:utf-8

from flask import Flask,request,url_for


app=Flask(__name__)

@app.route("/hello")
def hello():
	print("hello page")
	return "hello page"

@app.route("/index")
def index():
	print("index 被执行")

	a=1/0
	return "index pasge"


@app.before_first_request
def handel_before_first_request():
	"""第一次请求处理之前先被执行"""
	print("handel_before_first_request")

@app.before_request
def headdel_before_request():
	"""每次请求之前都被执行"""
	print("headdel_before_request 被执行")


@app.after_request
def headdel_after_request(response):
	"""在每次请求（视图函数处理）之后都被执行都被执行,前提是视图没有出现异常"""
	print("headdel_afder_request 被执行")
	return response


@app.teardown_request
def headdel_teardown_request(response):
	"""在每次请求（视图函数处理）之后都被执行都被执行，无论程序视图函数是否出现异常，都会被执行"""
	path=request.path
	if path==url_for("index"):
		print("在请求钩子中判断请求视图逻辑，index")
	elif path==url_for("hello"):
		print("在请求钩子中判断请求视图逻辑，hello")
	print("headdel_teardown_request 被执行")

	return response


if __name__ == '__main__':
	app.run(debug=False)