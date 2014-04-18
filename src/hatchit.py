#!/usr/bin/env python

from flask import abort, Flask, jsonify, redirect, render_template, request, session, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.secret_key = 'development'

@app.route('/')
def hello_world():
	return render_template('login2.html')

@app.route('/u/<user>')
@app.route('/user/<user>')
def get_user(user):
	pass
	
@app.route('/e/a', methods=['POST'])
@app.route('/e/add', methods=['POST'])
@app.route('/event/a', methods=['POST'])
@app.route('/event/add', methods=['POST'])
def add_event():
	if not session.get('logged_in'):
		redirect('/login')
	else:
		#TODO: add code for adding event
		pass

@app.route('/s/a', methods=['POST'])
@app.route('/s/add', methods=['POST'])
@app.route('/suggestion/a', methods=['POST'])
@app.route('/suggestion/add', methods=['POST'])
def add_suggestion():
	if not session.get('logged_in'):
		redirect('/login')
	else:
		return 'suggestion was added placeholder'
		#TODO: add code for suggestion
		pass

@app.route('/login', methods=['GET','POST'])
def fake_login():
	if request.method == 'GET':
		return 'login form goes here' #FIXME: create login form
	elif request.method == 'POST':
		request.form['user'] 

if __name__ == '__main__':
	app.run()

