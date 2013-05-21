#!/usr/bin/python
# -*- coding=utf-8 -*-

import os
import urllib2
import zipfile

__help__ = """This module will install Twitter bootstrap. If you use examples, the module will generate bootstrap-ready html files in templates directory! """


requirements = [ ]

directories = [
    "[base]"
    "[base]/[name]"
    "[base]/[name]/static"
    "[base]/[name]/static/bootstrap"
    "[base]/[name]/templates"
]

files = [ ]

def install(basepath, name):
    """
        Download Install Bootstrap files 
    """
    # http://twitter.github.io/bootstrap/assets/bootstrap.zip
    
    bootstrap_file_path = os.path.join(basepath, name, "static/bootstrap.zip")
    
    remote_file = urllib2.urlopen('http://twitter.github.io/bootstrap/assets/bootstrap.zip').read()
    localfile = open(bootstrap_file_path, 'w')
    localfile.write(remote_file)
    localfile.close()
    
    bootstrap_zip = zipfile.ZipFile(bootstrap_file_path)
    for f in bootstrap_zip.namelist():
        if f.endswith('/'):
            os.makedirs(f)
        else:
            bootstrap_zip.extract(f)
            
    return
    
def install_examples(basepath, name):
    """
        Install Bootstrap Templates files. ( examples )
    """
    #TODO
    return