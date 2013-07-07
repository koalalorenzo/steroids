#!/usr/bin/python
# -*- coding=utf-8 -*-
import os
import urllib2
import zipfile

__help__ = """This module will install AngularJS."""


requirements = [ ]

directories = [
    "[base]",
    "[base]/[name]",
    "[base]/[name]/static",
]

files = [ ]

def install(basepath, name):
    """
        Download Install AngularJS files 
    """
    # https://ajax.googleapis.com/ajax/libs/angularjs/1.0.7/angular.min.js
    
    static_files_path = os.path.join(basepath, name, "static/")
    angularjs_file_path = os.path.join(static_files_path,"angular.min.js")

    remote_file = urllib2.urlopen('https://ajax.googleapis.com/ajax/libs/angularjs/1.0.7/angular.min.js').read()
    localfile = open(angularjs_file_path, 'w')
    localfile.write(remote_file)
    localfile.close()
    
    return
    
def install_examples(basepath, name):
    """
        Install angularjs examples. 
    """
    
    return
