# coding:utf-8

from flask import Flask, current_app, redirect, url_for

from werkzeug.routing import BaseConverter
app=Flask(__name__)


#转换器
#192.168.146.1:5210/goods/123
#@app.route("/goods/<int:goods_id>")

@app.route("/goods/<goods_id>") # 不加转换器类型，默认是普通字符串规则（除啦/的字符）
def goods_detail(goods_id):
	"""定义视图函数"""
	return "goods detail page {}".format(goods_id)


# 1.定义自己的转换器
class MobileConverter(BaseConverter):
	def __init__(self,url_map):
		super(MobileConverter, self).__init__(url_map)
		self.regex=r"1[34578]\d{9}"


class RegexConverter(BaseConverter):
	def __init__(self,url_map,regex):
		# 调用父类初始化方法
		super(RegexConverter, self).__init__(url_map)
		# 将正则表达式的参数保存到对象的属性中，flask会去使用这个属性来进行路由的正则匹配
		self.regex=regex

	def to_python(self, value):
		"""可以使用to_python来过滤数据进行数据处理"""
		print("to_python方法被调用")
		#return "123"
		# value是在路径进行正则表达式匹配的时候提取的参数
		return value
	def to_url(self, value):
		"""使用url_for的方法时候被调用"""
		print("to_url被调用")
		return "15822222222"



# 2. 将自定义的转换器添加到flask的应用中
app.url_map.converters["re"]=RegexConverter
app.url_map.converters["mobile"]=MobileConverter


@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
#@app.route("/send/<mobile:mobile>")
def send_sms(mobile):

	return " send sms to {}".format(mobile)


@app.route("/index")
def index():
	url=url_for("send_sms",mobile='13588888888')
	return redirect(url)



if __name__ == '__main__':
	# 通过url_map可以查看整个flask中的路由
	print(app.url_map)
	app.run(host="0.0.0.0",port="5210",debug=True)