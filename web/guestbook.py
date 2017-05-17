# coding: utf-8
import shelve

from flask import Flask,request,render_template,redirect,escape,Markup

application = Flask(__name__)

DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    """保存提交的数据
    """
    #通过shelve模块打开数据库文件
    database = shelve.open(DATA_FILE)
    #如果数据库中没有greeting_list，就新建一个表
    if 'greeting_list' not in database:
    	greeting_list = []
    else:
    	#从数据库获取数据
    	greeting_list=database['greeting_list']
    #将提交的数据添加到表头
    greeting_list.insert(0,{
    	'name':name,
    	'comment':comment,
    	'create_at':create_at,
    	})
    #更新数据库
    database['greeting_list']=greeting_list
    #关闭数据库文件
    database.close()

def load_data():
	"""返回已提交的数据
	"""
	#通过shelve模块打开数据库文件
	database = shelve.open(DATA_FILE)
	#返回greeting_list,如果没有数据则返回空表
	greeting_list = database.get('greeting_list',[])
	database.close()
	return greeting_list

@application.route('/')
def index():
	'''首页
	使用模版显示页面
	'''
	return render_template('index.html')

if __name__ == '__main__':
	#在IP地址127.0.0.1的8000端口运行应用程序
	application.run('127.0.0.1',8000,debug=True)



