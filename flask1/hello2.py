# coding:utf-8

from flask import Flask,current_app

# 创建flask的应用对象
# __name__表示当前的模块的名字
#         模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app=Flask(
		__name__,
		static_url_path="/python" , # 访问静态资源的url前缀，默认是static
		static_folder="static", # 静态文件目录，默认就是static
		template_folder="templates" # 静态文件目录，默认就是templates
		)
# app=Flask(__main__)

# 配置文件使用方式
# 1.使用配置参数
# app.config.from_pyfile("config.cfg")

# 2.

# class Config(object):
# 	DEBUG = True
# 	ITCAST = "python"
#
#
# app.config.from_object(Config)

# 3

# app.config["DEBUG"]=True


@app.route("/")
def index():
	"""定义视图函数"""
	# a=1/0
	# 1.直接从全局对象app的config字典中取值
	# print(app.config.get("ITCAST"))
	# 2.current_app获取
	# print(current_app.config.get("ITCAST"))



	return "hello flask"


if __name__ == '__main__':
	app.run(host="0.0.0.0",port="5210",debug=True)