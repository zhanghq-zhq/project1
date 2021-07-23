# coding:utf-8

from flask import Flask,jsonify,request,make_response
import json

app=Flask(__name__)


@app.route("/set_cookie",methods=["GET"])
def index():
	resp=make_response("success")
	# 设置cookie，默认有效期是临时有效cookie，浏览器关闭失效
	resp.set_cookie("itcast","python1")
	# 通过max_age来设置有效期，单位：秒
	resp.set_cookie("itcast2","python2",max_age=3600)
	resp.headers["Set-Cookie3"]="itcast3=python3; Expires=Sat, 05-Dec-2020 05:20:41 GMT; Max-Age=3600; Path=/"
	return resp

@app.route("/get_cookie")
def get_cookie():
	c=request.cookies.get("itcast")
	return c

@app.route("/delete_cookie")
def delete_cookie():
	c=make_response(" delete success")
	# 删除cookie
	c.delete_cookie("itcast2")
	return c


if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5210",debug=True)