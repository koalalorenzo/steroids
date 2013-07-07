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
]

files = [ ]

def install(basepath, name):
    """
        Download Install socket.io files 
    """
    # https://raw.github.com/LearnBoost/socket.io-client/master/socket.io-client.js
    
    static_files_path = os.path.join(basepath, name, "static/")
    socketioclient_file_path = os.path.join(static_files_path,"socket.io-client.js")

    remote_file = urllib2.urlopen('https://raw.github.com/LearnBoost/socket.io-client/master/socket.io-client.js').read()
    localfile = open(socketioclient_file_path, 'w')
    localfile.write(remote_file)
    localfile.close()
    
    return
    
def install_examples(basepath, name):
    """
        Install socket.io examples. 
    """

    return
