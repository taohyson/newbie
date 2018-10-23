from flask import Flask
import pymongo
import json

app = Flask(__name__)

@app.route('/')
def index():
	return "<span style='color:red'>I am app 1</span>"

@app.route('/admin')
def admin():
	c = pymongo.MongoClient("mongodb://106.75.227.42:27017/")
	db = c['datav']
	col = db['t_admin']
	x = col.find_one()
	x['_id'] = str(x['_id'])
	return json.dumps(x)

@app.route('/view')
def view():
	c = pymongo.MongoClient("mongodb://106.75.227.42:27017/")
	db = c['datav']
	col = db['t_view']
	x = col.find_one()
	x['_id'] = str(x['_id'])
	return json.dumps(x)

$ uwsgi --http-socket 0.0.0.0:9090 --wsgi-file 部署Flask.py --callable app --processes 4 --threads 2