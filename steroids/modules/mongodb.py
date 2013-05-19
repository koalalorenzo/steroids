#!/usr/bin/python
# -*- coding=utf-8 -*-

import os

__help__ = """MongoDB (from "humongous") is an open-source document database, and the leading NoSQL database, written in C++.

This module provide integration with pymongo to save objects inside a MongoDB instance."""


requirements = [
    "pymongo"
]

directories = [
    "[base]/[name]",
    "[base]/[name]/objects",
]

files = [
    "[base]/configuration.py",
    "[base]/[name]/__init__.py",
    "[base]/[name]/database.py",
    "[base]/[name]/objects/__init__.py",
    "[base]/[name]/objects/Master.py",
]

def install(basepath, name):
    """
        Install MongoDB Module
    """
    
    objectMaster_file = open(os.path.join(basepath,"%s/objects/Master.py" % name), "w")
    objectMaster_file.write("""#!/usr/bin/env python
# -*- coding=utf-8 -*-

from pymongo.objectid import ObjectId
from %s.database import db

class Master(object):
    def __init__(self):
        self.id = ObjectId()
        self.database = db
        self.collection = str()
        
    def save(self):
        \"""
            Save the object in the database and overwrite if it already exists.
        \"""
        
        dictionary = self.__dict__()
        
        existing_dictionary = self.database[self.collection].find_one( { "id" : self.id } )
        if existing_dictionary:
            existing_dictionary.update(dictionary)
        else:
            existing_dictionary = dictionary
        self.database[self.collection].save(existing_dictionary)
        
    def load(self, id=None):
        \"""
            Load the object from the database
        \"""
        if not id:
            id = self.id
        if not id:
            raise Exception("No ID specified")
        
        dictionary = self.database.bookings.find_one( { "_id" : id } )
        self.by_dictionary(dictionary)
        return self
        
    def by_dictionary(self, dictionary, json=False):
        \"""
            This function loads the dictionary inside the object
        \"""
        self.id = dictionary['_id']
        if json:
            self.id = ObjectId(dictionary['_id'])
        
    def __dict__(self, json=False):
        \"""
            This function returns a dict of the Object.
        \"""
        output = dict()
        output['_id'] = self.id
        if not json:
            output['_id'] = str(self.id)
        
        return output""" % name )
    objectMaster_file.close()

    config_file = open(os.path.join(basepath,"configuration.py"), "a")
    config_file.write("""#MongoDB Configuration
MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DB = "%s" 

MONGO_USERNAME = "username"
MONGO_PASSWORD = "password"
    
""" % name)
    config_file.close()

    database_file = open(os.path.join(basepath,"%s/database.py" % name), "w")
    database_file.write("""from pymongo import Connection
from configuration import *

db_connection =  Connection(MONGO_HOST, MONGO_PORT)
db = db_connection[MONGO_DB]
db.authenticate(MONGO_USERNAME,MONGO_PASSWORD)
""")
    database_file.close()

    return
    
def install_examples(basepath, name):
    """
        Install MongoDB Module examples
    """
    
    example_file = open(os.path.join(basepath,"%s/objects/Example.py" % name), "w")
    example_file.write("""#!/usr/bin/env python
# -*- coding=utf-8 -*-

from pymongo.objectid import ObjectId
from %s.objects.Master import Master

class Example(Master):
    def __init__(self, database):
        super().__init__()
        self.dictionary = {"key":"value"}
        self.koalalorenzo = "is a great programmer"
        
        self.database = database
        self.collection = "Example"
        
    def by_dictionary(self, dictionary, json=False):
        \"""
            This function loads the dictionary inside the object
        \"""
        self.id = dictionary['_id']
        self.dictionary = dictionary['dictionary']
        self.koalalorenzo = dictionary['koalalorenzo']
        if json:
            self.id = ObjectId(dictionary['_id'])
        
    def __dict__(self, json=False):
        \"""
            This function returns a dict of the Object.
        \"""
        output = dict()
        output['_id'] = self.id
        output['dictionary'] = self.dictionary
        output['koalalorenzo'] = self.koalalorenzo
        
        if not json:
            output['_id'] = str(self.id)
        
        return output
""" % name)
    example_file.close()

    return