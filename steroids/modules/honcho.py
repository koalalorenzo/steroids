#!/usr/bin/python
# -*- coding=utf-8 -*-

import os

__help__ = """
"""


requirements = [
    "honcho"
]

directories = [ ]

files = [
    "[base]/Procfile"
]

def install(basepath, name):
    """
        Install Honcho/Foreman Module
    """
    proc_file = open(os.path.join(basepath,"Procfile"), "a")
    proc_file.write("web: python server.py\n")
    proc_file.close()
    return
    
def install_examples(basepath, name):
    """
        Install Honcho/Foreman Module examples
    """
    proc_file = open(os.path.join(basepath,"Procfile"), "a")
    proc_file.write("##Uncomment to enable:\n")
    proc_file.write("# web: python tornado.py # tornado web server\n")
    proc_file.write("# clock: python clock.py # clock / cron daemon\n")
    proc_file.close()
    return