# coding:utf-8


from flask import Flask,render_template,flash


app=Flask(__name__)

flag=True
app.config["SECRET_KEY"]="fsdfsdfds"

@app.route("/")
def macro():
	global flag
	if flag:
		flash("hello")
		flash("hello1")
		flash("hello2")
		flash("hello3")

		flag=False


	return render_template("macro.html")

if __name__ == '__main__':
	app.run(debug=True)