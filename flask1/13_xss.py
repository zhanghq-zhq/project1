# coding:utf-8

from flask import Flask,request,render_template
app=Flask(__name__)


@app.route("/xss",methods=["GET","POST"])
def index():
	text=""
	if request.method == "POST":
		text=request.form.get("text")

	return render_template("xss.html",text=text)

if __name__ == '__main__':

	app.run(host="0.0.0.0",port="5210",debug=True)