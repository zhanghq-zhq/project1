# coding:utf-8

from flask import request,Flask


app=Flask(__name__)



@app.route("/uoload",methods=["POST"])
def index():
	"""接收前端传送过来的文件"""
	file_obj=request.files.get("pic")
	if file_obj is None:
		# 表示没有发送文件
		return "未上传文件"
	# 将文件保存到本地
	# 1.创建一个文件

	# with open(r"C:\Users\Lenovo\Desktop\flask1\demo.png","wb") as wenjian:
	# 	data=file_obj.read()
	#
	# 	wenjian.write(data)

	file_obj.save(r"C:\Users\Lenovo\Desktop\flask1\123.png")

	return "文件上传成功"

if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5210",debug=True)