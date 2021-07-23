# coding:utf-8

from flask import Flask,render_template
app=Flask(__name__)

@app.route("/index")
def index():
	data={
		"name":"zhanghq",
		"age":"zhanghq",
		"my_dict":{"city":"shenzhen"},
		"my_list":[5,1,2,3,4,6],
		"my_int":0
	}
	return render_template("index.html",**data)


def list_step_2(list):
	"""自定义过滤器"""
	return list[::2]

# 注册过滤器第一个是过滤器的函数名，第二个是过滤使用名称

app.add_template_filter(list_step_2,"li2")


#过滤器第二种方法
@app.template_filter("li3")
def list_step_3(list):
	"""自定义过滤器"""
	return list[::3]




if __name__ == '__main__':

	app.run(host="0.0.0.0",port="5210",debug=True)