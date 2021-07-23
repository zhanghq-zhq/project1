# coding:utf-8

from flask import Flask,session,g


app=Flask(__name__)
#flask的session需要用到的秘钥字符串
app.config["SECRET_KEY"]="fdsfsdfsdf4546"

# flask默认吧session保存到cookie中
@app.route("/login",methods=["GET"])
def login():
	# 设置session数据
	session["name"]="python"
	session["mobile"]="13622222222"
	g.username="zhangsan"
	return "login success"

def say_hello():
	uaername=g.username




@app.route("/index")
def index():
	# 获取session数据
	name=session.get("name")
	return "hello {}".format(name)


if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5210",debug=True)