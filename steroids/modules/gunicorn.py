#!/usr/bin/python
# -*- coding=utf-8 -*-

import os
import stat   

__help__ = """Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.
"""


requirements = [
    "gunicorn"
]

directories = [ ]

files = [
    "[base]/start.sh"
]

def install(basepath, name):
    """
        Install gunicorn module
    """

    start_file_path = os.path.join(basepath,"start.sh")
    start_file = open(start_file_path, "a")
    start_file.write("#!/bin/bash\n")
    start_file.write("gunicorn server:app\n")
    start_file.close()

    old_perms = os.stat(start_file_path)
    os.chmod(start_file_path, old_perms.st_mode | stat.S_IEXEC)

    return
    
def install_examples(basepath, name):
    """
        Install gunicorn module examples
    """
    start_file = open(os.path.join(basepath,"start.sh"), "a")
    start_file.write("##Other commands examples:\n")
    start_file.write("# gunicorn server:app -k gevent # non blocking server\n")
    start_file.close()

    if os.path.exists(os.path.join(basepath,"Procfile")):
        proc_file = open(os.path.join(basepath,"Procfile"), "a")
        proc_file.write("# Gunicorn commands examples:\n")
        proc_file.write("# web: gunicorn server:app # gunicorn server \n")
        proc_file.write("# web: gunicorn server:app -k gevent # non blocking server\n")
        proc_file.close()

    return