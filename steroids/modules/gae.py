import os
import sys

__help__ = """Google App Engine (gae)

To use Google App Engine correctly with other modules ( ex: flask ) you 
should use this command to install everything in your working directory:

sudo pip install -U -r requirements.txt -t $PWD/modules

This command will download and install all everything gae needs into the
current directory.
"""


requirements = [
    ""
]

directories = [
    "[base]",
    "[base]/modules"
    "[base]/[name]"
    "[base]/[name]/objects"
    ]

files = [
    "[base]/app.yaml",
    "[base]/gae.py",
    ]

def install(basepath, name):
    """
        Install Tornado Module
    """
    
    gae_yaml_file = open(os.path.join(basepath,"app.yaml"), "w")
    gae_yaml_file.write("""application: %s
version: 1
runtime: python27
api_version: 1
threadsafe: yes

handlers:
- url: .*
  script: gae.py
""" % name)
    gae_yaml_file.close()

    gae_py_file = open(os.path.join(basepath,"gae.py"), "w")
    gae_py_file.write("""from google.appengine.ext.webapp.util import run_wsgi_app

import os
import sys
sys.path.append(os.path.join(os.getcwd(),"modules"))

from %s import app
run_wsgi_app(app)
""" % name)
    gae_py_file.close()

    return
    
def install_examples(basepath, name):
    """
        Install Tornado Module with example files
    """

    gae_object_example = open(os.path.join(basepath,name,"objects/Example.py"), "w")
    gae_object_example.write("""

""" )
    gae_object_example.close()

    return