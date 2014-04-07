#!/usr/bin/env python

from flask import Flask, redirect, render_template, request, session, url_for
from flask_oauthlib.client import OAuth, OAuthException

app = Flask(__name__)
app.config['FACEBOKK_APP_ID'] = ''
app.config['FACEBOOK_APP_SECRET'] = ''
app.config['GOOGLE_APP_ID'] = ''
app.config['GOOGLE_APP_SECRET'] = ''
app.secret_key = 'development'
oauth = OAuth(app)

facebook = oauth.remote_app(
	'facebook',
	consumer_key = app.config.get('FACEBOOK_APP_ID'),
	consumer_secret = app.config.get('FACEBOOK_APP_SECRET'),
	request_token_params = {'scope' : 'email'},
	base_url = 'https://graph.facebook.com',
	request_token_url = None,
	access_token_url = '/oauth/access_token',
	authorize_url = 'https://www.facebook.com/dialog/oauth'
)

google = oauth.remote_app(
	'google',
	consumer_key = app.config.get('GOOGLE_APP_ID'),
	consumer_secret = app.config.get('GOOGLE_APP_SECRET'),
	request_token_params = {'scope' : 'https://www.googleapis.com/auth/userinfo.email'},
	base_url = 'https://www.googleapis.com/oauth2/v1/',
	request_token_url = None,
	access_token_url = 'https://accounts.google.com/o/auth2/token',
	authorize_url = 'https://accounts.google.com/o/oauth2/auth'
)

@app.route('/')
def hello_world():
	return render_template('base.html')

@facebook.togengetter
def get_facebook_oauth_token():
	return session.get('facebook_token')

@google.tokengetter
def get_google_oauth_token():
	return session.get('google_token')

if __name__ == '__main__':
	app.run()

