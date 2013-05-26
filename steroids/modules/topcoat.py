#!/usr/bin/python
# -*- coding=utf-8 -*-

import os
import urllib2
import zipfile
import shutil

__help__ = """This module will install topcoat css style. Version: 0.3.0"""

requirements = [ ]

directories = [
    "[base]",
    "[base]/[name]",
    "[base]/[name]/static",
    "[base]/[name]/static/topcoat",
    "[base]/[name]/templates",
]

files = [ 
    "[base]/[name]/templates/topcoat.html",
]

def install(basepath, name):
    """
        Download Install Topcoat 0.3.0 files 
    """
    # https://github.com/topcoat/topcoat/archive/0.3.0.zip
    
    static_files_path = os.path.join(basepath, name, "static/")
    final_files_path = os.path.join(basepath, name, "static/topcoat")
    temporary_files_path = os.path.join(basepath, name, "static/topcoat/temporary")
    topcoat_file_path = os.path.join(static_files_path, "topcoat.zip")
    
    os.makedirs(temporary_files_path)
    
    remote_file = urllib2.urlopen('http://github.com/topcoat/topcoat/archive/0.3.0.zip').read()
    localfile = open(topcoat_file_path, 'w')
    localfile.write(remote_file)
    localfile.close()

    current_dir = os.getcwd()
    topoact_zip = zipfile.ZipFile(topcoat_file_path)
    os.chdir(temporary_files_path)
    for f in topoact_zip.namelist():
        if f.endswith('/'):
            new_directory = os.path.join(temporary_files_path,f)
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)
        else:
            topoact_zip.extract(f)
    os.chdir(current_dir)
    os.remove(topcoat_file_path)
    
    release_files_path = os.path.join(temporary_files_path,"topcoat-0.3.0/release")
    shutil.move(os.path.join(release_files_path,"css"), final_files_path)
    shutil.move(os.path.join(release_files_path,"font"), final_files_path)
    shutil.move(os.path.join(release_files_path,"img"), final_files_path)
    shutil.rmtree(temporary_files_path)

    topcoat_layout_file = open(os.path.join(basepath,name,"templates/topcoat.html"), "w")
    topcoat_layout_file.write("""<html>
    <head>
        <title>%s {%% block title %%}{%% endblock %%}</title>

        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="/static/topcoat/css/topcoat-mobile-light.min.css">
        
        <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
          <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
        {%% block head %%}{%% endblock %%}
    </head>
    <body>
        {%% block header %%}{%% endblock %%}
        {%% block container %%}{%% endblock %%}
        %s is powered by <a href="http://projects.setale.me/Steroids">Steroids</a>
        {%% block footer %%}{%% endblock %%}
    </body>    
</html>""" % (name, name))
    topcoat_layout_file.close()
    
    return
    
def install_examples(basepath, name):
    """
        Install Topcoat 0.3.0 Templates files. ( examples )
    """
    bootstrap_example_file = open(os.path.join(basepath,name,"templates/homeExample/homepage.html"), "w")
    bootstrap_example_file.write("""{% extends "topcoat.html" %}

{% block container %}
<h1>Hello World!</h1>
<div>
    This is an example using Topcoat!
</div>
{% endblock %}
""")
    bootstrap_example_file.close()
    
    return