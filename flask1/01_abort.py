# coding:utf-8

from flask import request,Flask,abort,Response


app=Flask(__name__)


@app.route("/login",methods=["GET"])
def index():
	# name=request.form.get()
	# pwd=request.form.get()

	name=""
	pwd=""
	if name != "zhangsan" or pwd!="123456":
		# 使用abort函数可以立即终止视图的执行
		# 饼可以返回给前段特定的方法
		# 1传递状态吗信息，必须是标准的http状态吗
		abort(404)
		# 2.传递响应体信息
		# resp=Response("login failed")
		# abort(resp)
	else:
		return "登录失败"


# 定义错误处理方法
@app.errorhandler(404)
def handle_404_error(error):
	"""自定义的处理错误方法"""
	# 这个函数的返回值会是前段用户最终看到的结果
	return "出现了4040错误，错误信息：{}".format(error)


if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5210",debug=True)