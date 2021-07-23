# coding:utf-8

from flask import Flask,jsonify
import json

app=Flask(__name__)


@app.route("/index",methods=["GET"])
def index():
	"""json就是字符串"""
	data={
		"name":"python",
		"age":30
	}
	# json.dumps(字典)，将Python的字典转换为json字符串
	# json.loads(字符串)，将Python的字符串转换为Python字典
	# return json.dumps(data),200,{"Content-Type":"application/json"}
	# jsonfy帮助我们转化为json数据，并设置响应头Content-Type为application/json
	# 也可以使用参数方式，返回前段的也是json
	return jsonify(age=25,name="zhangsan")
if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5210",debug=True)