#!/usr/bin/python
# -*- coding=utf-8 -*-

import os
import string
import random

__help__ = """ Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. """


requirements = [
    "flask"
]

directories = [
    "[base]/[name]",
    "[base]/[name]/templates",
    "[base]/[name]/static",
    "[base]/[name]/views",
]

files = [
    "[base]/settings.py",
    "[base]/server.py",
    "[base]/[name]/__init__.py",
    "[base]/[name]/constants.py",
    "[base]/[name]/decorators.py",
    "[base]/[name]/views/__init__.py",
]

def install(basepath, name):
    """
        Install Flask Module
    """
    
    init_file = open(os.path.join(basepath,"%s/__init__.py" % name), "w")
    init_file.write("""#!/usr/bin/python
# -*- coding=utf-8 -*-

\"""%s: Project Based on Steroids\"""

__version__ = "0.1"
__author__ = "Your Name ( http://projects.setale.me/Steroids )"
__author_email__ = "your_super_email_addr@domain.com"
__license__ = ""
__copyright__ = "Copyright (c) 2013, 2014 Somebody"

from flask import Flask
from flask import url_for
from flask import redirect

from settings import *

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

# Static Files
@app.route('/static/<path:afilepath>')
def serve_static(afilepath):
    return redirect(url_for('static', filename=afilepath))

# Import Views here:
# Ex: import %s.views.ViewName
""" % (name, name))

    random_value = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    config_file = open(os.path.join(basepath,"settings.py"), "a")
    config_file.write("""# -*- coding=utf-8 -*-
    
# Flask Config
FLASK_SECRET_KEY = "%s"
SERVER_PORT = 8080
SERVER_HOST = "0.0.0.0"
FLASK_DEBUG = True
""" % random_value)
    
    server_file = open(os.path.join(basepath,"server.py"), "w")
    server_file.write("""
from %s import app
from settings import FLASK_DEBUG, SERVER_PORT, SERVER_HOST

app.debug = FLASK_DEBUG
if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=SERVER_PORT)
""" % name)
    
    
    return
    
def install_examples(basepath, name):
    """
        Install Flask Module
    """
    
    init_file = open(os.path.join(basepath,"%s/__init__.py" % name), "a")
    init_file.write("\nimport %s.views.homeExample\n" % name)
    init_file.close()
    
    example_file = open(os.path.join(basepath,"%s/views/homeExample.py" % name), "w")
    example_file.write("""#!/usr/bin/python
# -*- coding=utf-8 -*-
from %s import app
from %s.decorators import *
from %s.constants import *

from flask import render_template
from flask import url_for
from flask import session
from flask import abort
from flask import redirect
from flask import flash

@app.route("/")
def homeExample_homepage():
    return render_template("homeExample/homepage.html")

""" % (name, name, name))
    example_file.close()
    
    example_template_layout_file = open(os.path.join(basepath,"%s/templates/layout.html" % name), "w")
    example_template_layout_file.write("""<html><head><title>Steroids</title></head><body>
<hr>
{%% block container %%}
{%% endblock %%}
<hr>
%s is powered by <a href="http://projects.setale.me/Steroids">Steroids</a>
</body></html>""" % name)
    example_template_layout_file.close()   
    
    if not os.path.exists(os.path.join(basepath,"%s/templates/homeExample" % name)):
        os.mkdir(os.path.join(basepath,"%s/templates/homeExample" % name))
    
    example_template_file = open(os.path.join(basepath,"%s/templates/homeExample/homepage.html" % name), "w")
    example_template_file.write("""{% extends "layout.html" %}

{% block container %}
<h1>Hello World!</h1>
This is an example!
{% endblock %}

""")
    example_template_file.close()   
    
    return