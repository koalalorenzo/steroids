import os

__help__ = """Create Google App Engine.
"""


requirements = [
    ""
]

directories = [
    "[base]",
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
from %s import app
run_wsgi_app(app)
""" % name)
    gae_py_file.close()

    return
    
def install_examples(basepath, name):
    """
        Install Tornado Module with example files
    """
    return