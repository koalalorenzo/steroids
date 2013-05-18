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
__author__ = "Lorenzo Setale ( http://projects.setale.me/Steroids )"
__author_email__ = "koalalorenzo@gmail.com"
__license__ = "See: http://creativecommons.org/licenses/by-nd/3.0/ "
__copyright__ = "Copyright (c) 2013, 2014 Lorenzo Setale"

from flask import Flask
from flask import url_for
from flask import redirect

from configuration import *

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

# Static Files
@app.route('/static/<path:afilepath>')
def serve_static(afilepath):
    return redirect(url_for('static', filename=afilepath))

# Import Views here:
# Ex: import %s.views.ViewName
""" % (name, name))
    
    return
    
def install_examples(basepath, name):
    """
        Install Flask Module
    """
    
    init_file = open(os.path.join(basepath,"%s/__init__.py" % name), "a")
    init_file.write("\nimport %s.views.homeExample\n")
    init_file.close()
    
    example_file = open(os.path.join(basepath,"%s/views/homeExample.py" % name), "w")
    example_file.write("""#!/usr/bin/python
# -*- coding=utf-8 -*-
from %s import app
from %s.decorators import *
from %s.conventions import *

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
{% block container %}
{% endblock %}
<hr>
%s is powered by <a href="http://setale.me/Steroids">Steroids</a>!
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

""" % (name, name, name))
    example_template_file.close()   
    
    return