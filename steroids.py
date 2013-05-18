#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.getcwd())

import steroids.modules 
import argparse
import imp


parser = argparse.ArgumentParser(description="Python Flask with Steroids")
parser.add_argument('action', help="Action to perform", choices=["init", "run", "upgrade"])
parser.add_argument('name', help="Project name")

parser.add_argument('--modules', '-m', nargs="*", default=["flask","mongodb","tornado","honcho"], help="Modules to use")
parser.add_argument('--port', '-p', nargs=1, default=[8080], help="Default http port to use")
parser.add_argument('--basepath', '-b', nargs=1, default=os.getcwd(), type=str, help="Default base path to use")
parser.add_argument('--examples', '-e', nargs=1, default=False, type=bool, help="Install examples")

arguments = parser.parse_args()
    
# Variables:    
PROJECT_NAME = arguments.name
PROJECT_ABS_PATH = os.path.join(arguments.basepath,PROJECT_NAME)
PROJECT_PORT = arguments.port[0]
PROJECT_MODULES = list()

if arguments.modules:
    modules_available = dir(steroids.modules)
    for module in arguments.modules:
        if module in modules_available:
            PROJECT_MODULES.append(module)
        else:
            sys.stderr.write("\nW: 404 module not found: %s\n" % module)

if arguments.action == "init":
    from steroids.installation import *
    
    if not os.path.exists(PROJECT_ABS_PATH):
        os.mkdir(PROJECT_ABS_PATH)
    
    sys.stderr.write("Installing Modules:\n")
    
    all_requirementes = list()
    for module_name in PROJECT_MODULES:
        module = __import__("steroids.modules.%s" % module_name, globals(), locals(), [module_name], -1)
        sys.stderr.write(" - Installing %s\n" % module_name)
        install_module(module, PROJECT_ABS_PATH, PROJECT_NAME, examples=arguments.examples)
        all_requirementes = all_requirementes + list(set(module.requirements) - set(all_requirementes))
    
    sys.stderr.write("Creating requirements: ")
    requirements_file = open(os.path.join(PROJECT_ABS_PATH,"requirements.txt"), "w")
    requirements_file.write("\n".join(all_requirementes))
    requirements_file.close()
    sys.stderr.write("done\n")
    
    