# coding:utf-8

from flask import Flask,session


app=Flask(__name__)




@app.route("/index")
def index():
	print("index 被执行")

	a=1/0
	return "index pasge"


@app.route("/hello")
def hello():
	print("hello")
	return "hello page"


@app.after_request
def tt_after_request(response):
	print("after_request")
	return response



if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5210")