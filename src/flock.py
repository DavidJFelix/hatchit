#!/usr/bin/env python

from flask import Flask, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'development'

@app.route('/')
def hello_world():
	return render_template('base.html')

if __name__ == '__main__':
	app.run()

