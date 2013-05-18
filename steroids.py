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
parser.add_argument('action', help="Action to perform", choices=["init", "run"])
parser.add_argument('name', help="Project name")

parser.add_argument('--modules', '-m', nargs="*", default=["mongodb","tornado","honcho"], help="Modules to use")
parser.add_argument('--port', '-p', nargs=1, default=[8080], help="Default http port to use")
parser.add_argument('--basepath', '-b', nargs=1, default=os.getcwd(), type=str, help="Default base path to use")

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

sys.stderr.write("Using:\n")    
print PROJECT_NAME
print PROJECT_ABS_PATH
print PROJECT_PORT
print PROJECT_MODULES

if arguments.action == "init":
    if not os.path.exists(PROJECT_ABS_PATH):
        os.mkdir(PROJECT_ABS_PATH)
    
    