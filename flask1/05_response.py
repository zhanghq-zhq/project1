# coding:utf-8

from flask import request,Flask,make_response


app=Flask(__name__)


@app.route("/index",methods=["GET"])
def index():
	# 1.使用元组，返回指定义的响应信息
	# 		响应体 、状态吗、响应头
	# return "index page",400,[("itcast","python"),("city","shenzhen")]
	# return "index page",400,{"itcastl":"python","age":30,"city":"shenzhen"}
	# 可以指定返回的状态吗
	# return "index page",666,{"itcastl":"python","age":30,"city":"shenzhen"}
	# 字符串的方式传状态吗，字符串的方式定义状态吗，第一个是状态吗空格分隔第二个是状态吗的说明信息
	# return "index page","666 itcast status",{"itcastl":"python","age":30,"city":"shenzhen"}
	# 可以不传响应头，响应体是有顺序的（响应体、状态吗、响应头），可以从后面开始省略，不能从中间省略
	# return "index page","666 itcast status"

	# 2.是有make_response来构造响应信息
	resp=make_response("index page 2")
	resp.status= "999 itcast" # 设置状态吗
	resp.headers["city"]="is" # 设置响应头
	return resp


if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5210",debug=True)