#!/usr/bin/env python

from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.secret_key = 'development'

@app.route('/')
def hello_world():
	return render_template('base.html')

@app.route('/u/<user>')
@app.route('/user/<user>')
def get_user(user):
	pass
	
@app.route('/e/a', methods=['POST'])
@app.route('/e/add', methods=['POST'])
@app.route('/event/a', methods=['POST'])
@app.route('/event/add', methods=['POST'])
def add_event():
	pass

@app.route('/s/a', methods=['POST'])
@app.route('/s/add', methods=['POST'])
@app.route('/suggestion/a', methods=['POST'])
@app.route('/suggestion/add', methods=['POST'])
def add_suggestion():
	pass

if __name__ == '__main__':
	app.run()

