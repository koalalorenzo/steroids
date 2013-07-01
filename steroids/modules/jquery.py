#!/usr/bin/python
# -*- coding=utf-8 -*-

import os
import urllib2
import zipfile

__help__ = """This module will install jquery."""


requirements = [ ]

directories = [
    "[base]",
    "[base]/[name]",
    "[base]/[name]/static",
]

files = [ ]

def install(basepath, name):
    """
        Download Install jquery files 
    """
    # http://twitter.github.io/bootstrap/assets/bootstrap.zip
    
    static_files_path = os.path.join(basepath, name, "static/")
    jquery_file_path = os.path.join(static_files_path,"jquery.min.js")

    remote_file = urllib2.urlopen('http://code.jquery.com/jquery-latest.min.js').read()
    localfile = open(jquery_file_path, 'w')
    localfile.write(remote_file)
    localfile.close()
    
    return
    
def install_examples(basepath, name):
    """
        Install jquery examples. 
    """
    #TODO

    return