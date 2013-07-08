#!/usr/bin/python
# -*- coding=utf-8 -*-
import os
import urllib2
import zipfile

__help__ = """This module will install socket.io javascript client and python module (gevent-socketio)."""


requirements = [ 
"gevent-socketio"
]

directories = [
    "[base]",
    "[base]/[name]",
    "[base]/[name]/static",
    "[base]/[name]/templates",
    "[base]/[name]/views",
]

files = [ ]

def install(basepath, name):
    """
        Download Install socket.io files 
    """
    # https://raw.github.com/LearnBoost/socket.io-client/master/socket.io-client.js
    
    static_files_path = os.path.join(basepath, name, "static/")
    socketioclient_file_path = os.path.join(static_files_path,"socket.io.js")

    remote_file = urllib2.urlopen('https://raw.github.com/LearnBoost/socket.io-client/master/socket.io-client.js').read()
    localfile = open(socketioclient_file_path, 'w')
    localfile.write(remote_file)
    localfile.close()

    templates_path = os.path.join(basepath,name,"templates")
    template_socketio = open(os.path.join(templates_path, "socketio.html"), "w")
    template_socketio.write("""<html>
    <head>
        <title>%s {%% block title %%}{%% endblock %%}</title>
        <meta charset="utf-8">
        <script src="//code.jquery.com/jquery.min.js"></script>
        <script src="/static/socket.io-client.js"></script>
        {%% block head %%}{%% endblock %%}
    </head>
    <body>
        {%% block header %%}{%% endblock %%}
        {%% block container %%}{%% endblock %%}
        {%% block footer %%}{%% endblock %%}
    </body>
</html>""" % name)
    template_socketio.close()

    views_path = os.path.join(basepath,name,"views")
    template_alert_users = open(os.path.join(views_path, "websockets.py"), "w")
    template_alert_users.write("""from %s import app
from %s.decorators import *
from %s.constants import *

from flask import render_template
from flask import url_for
from flask import session
from flask import request
from flask import abort
from flask import redirect
from flask import flash
from flask import send_from_directory

from socketio import socketio_manage
from socketio.namespace import BaseNamespace

class CustomNamespace(BaseNamespace):
    def __init__(self, *args, **kwargs):
        request = kwargs.get('request', None)
        self.ctx = None
        if request:
            self.ctx = current_app.request_context(request.environ)
            self.ctx.push()
            current_app.preprocess_request()
            del kwargs['request']
        super(BaseNamespace, self).__init__(*args, **kwargs)

    def disconnect(self, *args, **kwargs):
        if self.ctx:
            self.ctx.pop()
        super(BaseNamespace, self).disconnect(*args, **kwargs)

    def on_alert():
        self.emit("alert");

@app.route('/socket.io/socket.io.js')
def socketio_static():
    return send_from_directory('static', "socket.io.js"))

@app.route('/socket.io/<path:tpath>')
def socketio_run(tpath):
    real_request = request._get_current_object()
    socketio_manage(request.environ, {'/alerter': CustomNamespace},
            request=real_request)
    return Response()

""" % (name, name, name))
    template_alert_users.close()

    init_file = open(os.path.join(basepath, name, "__init__.py"), "a")
    init_file.write("\nimport %s.views.websockets\n" % name)
    init_file.close()
    
    return
    
def install_examples(basepath, name):
    """
        Install socket.io examples. 
    """

    examples_tempaltes_path = os.path.join(basepath,name,"templates","examples")
    if not os.path.exists(examples_tempaltes_path):
        os.mkdir(examples_tempaltes_path)

    examples_template_alert_path = os.path.join(examples_tempaltes_path,"websockets")
    if not os.path.exists(examples_template_alert_path):
        os.mkdir(examples_template_alert_path)

    template_alert_users = open(os.path.join(examples_template_alert_path, "alert.html"), "w")
    template_alert_users.write("""{% extends "socketio.html" %}

{% block container %}
<h1>Hello world!</h1>
<div class="hero-unit">
    <p class="lead">
        <a class="btn btn-large" href="javascript:void(0);" onclick="alertUsers();">alert every users connected</a>
    <p>
</div>

<script>
  var alerter = io.connect('http://localhost/alerter')
  
  alerter.on('connect', function () {
    alert("!!!");
  });

  function alertUsers() {
    alerter.emit("alert");
  }
</script>
{% endblock %}

    """)
    template_alert_users.close()


    views_path = os.path.join(basepath,name,"views")
    view_example_files = open(os.path.join(views_path, "websockets.py"), "a")
    view_example_files.write("""

# SocketIo Example:
@app.route('/alerter')
def socketio_alerter():
    return render_template("examples/websockets/alert.html")

""" )
    view_example_files.close()



    return
