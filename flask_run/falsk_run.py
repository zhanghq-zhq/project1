from flask import Flask,request
import pytest
import os
import time
from os.path import dirname,abspath,join
from config import basedir
# 项目路径


testcase=join(basedir,'test','test_api')
print(testcase)
app=Flask(__name__)

@app.route("/api")
def demo():
    dirs = os.listdir(basedir+r"\report")
    list_data=""
    for file_name in dirs:
        if 'html' in file_name:
            url=join(r'http://localhost:63342\project1\report',file_name)
            list_data+=f"<a href='{url}'>{file_name}</a>&nbsp;&nbsp;&nbsp;&nbsp;"
    return f"""
    <h2>执行接口测试用例</h2>
    <h3>
        一.冒烟测试输入A&nbsp;&nbsp;&nbsp;&nbsp;
        二.测试msg输入B <hr>
        三.日志测试输入C &nbsp;&nbsp;&nbsp;&nbsp;
        四.回归全部接口测试输入 <hr>
    </h3>
    <form method="post" action="/testapi">
        <input type="text" name="mark" >
        <input type="submit" value="提交" >
        <hr>
        <h2>测试报告</h2>
        {list_data}
    </form>
    """




@app.route("/testapi",methods=["POST"])
def run():
    run_data=request.form['mark']
    if run_data == 'A' or run_data=='a':
        pytest.main([testcase, '-v',rf'--html={basedir}\report\report.html'])

        dirs = os.listdir(basedir+r"\report")

        for file_name in dirs:
            time.sleep(2)
            if 'report' in file_name:
                now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                report_name=now_time.replace(" ","-").replace(":","-")
                lod=rf"{basedir}\report\report.html"
                now=rf"{basedir}\report\api-冒烟测试-{report_name}.html"
                print(lod)
                print(now)
                os.rename(lod,now)

    elif run_data == 'B' or run_data == 'b':
        pytest.main([testcase, '-v', r'--html=E:\project1\report\report.html'])

        dirs = os.listdir(basedir+r"\report")

        for file_name in dirs:
            time.sleep(2)
            if 'report' in file_name:
                now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                report_name = now_time.replace(" ", "-").replace(":", "-")
                os.rename(r"E:\project1\report\report.html", rf"E:\project1\report\api-消息-{report_name}.html")
    else:
        return "你输入错误，请重新输入"
    return "执行完成"



if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8865')