# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)


class Config():
	"""配置参数"""
	#sqlalchemy的配置参数

	SQLALCHEMY_DATABASE_URI="mysql://root:root@127.0.0.1:3306/db_python04"
	# 设置SQLAlchemy自动跟踪数据库

	#SQLALCHEMY_TRACK_MODIFICACTIONS=True


app.config.from_object(Config)

# 创建数据库SQLAlchemy工具对象

db=SQLAlchemy(app)


class Role(db.Model):
	"""用户角色表"""
	__tablename__ = "tbl_roles"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32), unique=True)

	users = db.relationship("User",backref="role")


# 表名常见命名规范
# iHome-> ih_user 数据库缩写_表名
# tbl_user tbl_表名

# 创建数据库类型
class User(db.Model):
	__tablename__="tbl_users"
	id=db.Column(db.Integer,primary_key=True) # 整型的主键，会默认设置为自增主键
	name=db.Column(db.String(64),unique=True)
	email=db.Column(db.String(128),unique=True)
	password=db.Column(db.String(128))
	role_id=db.Column(db.Integer,db.ForeignKey("tbl_roles.id"))




if __name__ == '__main__':
	# 清楚数据库的所有数据
	db.drop_all()

	# 创建所有的表
	db.create_all()

