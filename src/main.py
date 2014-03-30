#!/usr/bin/env python

import cherrypy
from jinja2 import Environment, FileSystemLoader

j2_env = Environment(loader = FileSystemLoader('templates'))

class Root(object):
	@cherrypy.expose
	def index(self):
		template = j2_env.get_template('base.html')
		return template.render()

cherrypy.config.update({'server.socket_port':5000})
cherrypy.quickstart(Root())
