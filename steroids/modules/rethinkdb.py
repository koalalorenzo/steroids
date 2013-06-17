#!/usr/bin/python
# -*- coding=utf-8 -*-

import os

__help__ = """RethinkDB: An open-source distributed database built with love.

This module provide integration with rethinkdb to save objects inside a RethinkDB instance."""


requirements = [
    "rethinkdb"
]

directories = [
    "[base]/[name]",
    "[base]/[name]/objects",
]

files = [
    "[base]/settings.py",
    "[base]/[name]/__init__.py",
    "[base]/[name]/objects/__init__.py",
    "[base]/[name]/objects/Master.py",
]

def install(basepath, name):
    """
        Install RethinkDB Module
    """
    
    objectMaster_file = open(os.path.join(basepath,"%s/objects/Master.py" % name), "w")
    objectMaster_file.write("""#!/usr/bin/env python
# -*- coding=utf-8 -*-
import rethinkdb as r
import json


class Master(object):
    def __init__(self):
        self.id = None

        self._connection = None
        self._database = None
        self._collection = str()

    def connect(self, host, port, dbname, collection=None, username=None, password=None):
        \"""
            This function will connect the object to the database. 
        \"""
        return 

    def save(self):
        \"""
            Save the object in the database and overwrite if it already exists.
        \"""
        
        dictionary = self.__dict__()
        
        return

    def delete(self):
        \"""
            Delete the object in the database
        \"""
        
        return

    def load(self, oid=None):
        \"""
            Load the object from the database
        \"""
        return self

        
    def load_by_query(self, query):
        \"""
            Load object from query specific query
        \"""

        return self

    def find_objects(self, query, limit=100, page=0):
        \"""
            Find all the objects with a specific query
        \"""
        
        return list()
    
    def find_all(self, limit=100, page=0):
        \"""
            Find all the objects
        \"""
        return list()

    def by_dictionary(self, dictionary, json=False):
        \"""
            This function loads the dictionary inside the object
        \"""
        return
        
    def __dict__(self, json=False):
        \"""
            This function returns a dict of the Object.
        \"""
        output = dict()
        return output
        
    def __json__(self, json=False):
        \"""
            This function returns a json dict of the Object.
        \"""
        return json.dumps(self.__dict__(json=True))
""" % name )
    objectMaster_file.close()

    config_file = open(os.path.join(basepath,"settings.py"), "a")
    config_file.write("""#RethinkDB Configuration
# for MyObject.connect(...) 
RETHINKDB_HOST = "127.0.0.1"
RETHINKDB_PORT = 27017
RETHINKDB_DB = "%s" 

RETHINKDB_NEEDS_AUTH = False
RETHINKDB_USERNAME = "username"
RETHINKDB_PASSWORD = "password"
    
""" % name)
    config_file.close()

    return
    
def install_examples(basepath, name):
    """
        Install RethinkDB Module examples
    """
    
    example_file = open(os.path.join(basepath,"%s/objects/Example.py" % name), "w")
    example_file.write("""#!/usr/bin/env python
# -*- coding=utf-8 -*-

from %s.objects.Master import Master

class Example(Master):
    def __init__(self, database):
        super( Master, self ).__init__()
        self.id = ""
        
        self.dictionary = {"key":"value"}
        self.koalalorenzo = "is a great programmer"
        
        self._database = database
        self._collection = "Example"
        
    def by_dictionary(self, dictionary, json=False):
        \"""
            This function loads the dictionary inside the object
        \"""
        self.id = dictionary['id']
        self.dictionary = dictionary['dictionary']
        self.koalalorenzo = dictionary['koalalorenzo']
        if json:
            self.id = dictionary['id']
        
    def __dict__(self, json=False):
        \"""
            This function returns a dict of the Object.
        \"""
        output = dict()
        output['id'] = self.id
        output['dictionary'] = self.dictionary
        output['koalalorenzo'] = self.koalalorenzo
        
        if not json:
            output['id'] = str(self.id)
        
        return output

""" % name)
    example_file.close()

    return