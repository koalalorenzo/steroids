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
    "[base]/settings.py",
    "[base]/[name]/__init__.py",
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

from pymongo import Connection
from pymongo.objectid import ObjectId
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

        self._connection =  Connection(host, port)
        self._database = self._connection[dbname]
        if username and password:
            self._database.authenticate(username,password)

    def save(self):
        \"""
            Save the object in the database and overwrite if it already exists.
        \"""
        
        dictionary = self.__dict__()
        
        existing_dictionary = self._database[self._collection].find_one( { "_id" : ObjectId(self.id) } )
        if existing_dictionary:
            existing_dictionary.update(dictionary)
        else:
            existing_dictionary = dictionary
        newId = self._database[self._collection].save(existing_dictionary)
        if not self.id:
            self.id = newId

    def delete(self):
        \"""
            Delete the object in the database
        \"""
        
        existing_dictionary = self._database[self._collection].remove( { "_id" : ObjectId(self.id) } )
        self = None

    def load(self, oid=None):
        \"""
            Load the object from the database
        \"""
        if not oid:
            oid = self.id
        if not oid:
            raise Exception("No ID specified")

        return self.load_by_query( { "_id" : ObjectId(oid) } )
        
    def load_by_query(self, query):
        \"""
            Load object from query specific query
        \"""
        dictionary = self._database[self._collection].find_one( query )
        if not dictionary:
            raise Exception("Not found")
        self.by_dictionary(dictionary)
        return self

    def find_objects(self, query, limit=100, page=0):
        \"""
            Find all the objects with a specific query
        \"""
        query = self._database[self._collection].find(query)
        query.limit(limit)
        if page > 0:
            query.skip(int(limit*page))

        objects = list()
        for data in query:
            new_object = self.__class__()
            new_object.database = self._database
            new_object.by_dictionary(data)
            objects.append(new_object)
        return objects
    
    def find_all(self, limit=100, page=0):
        \"""
            Find all the objects
        \"""
        return self.find_objects({}, limit=limit, page=page)

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
        if self.id:
            output['_id'] = self.id
        if not json:
            output['_id'] = str(self.id)
        
        return output
        
    def __json__(self, json=False):
        \"""
            This function returns a json dict of the Object.
        \"""
        return json.dumps(self.__dict__(json=True))
""" )
    objectMaster_file.close()

    config_file = open(os.path.join(basepath,"settings.py"), "a")
    config_file.write("""#MongoDB Configuration
# for MyObject.connect(...) 

MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DB = "%s" 

MONGO_NEEDS_AUTH = False
MONGO_USERNAME = "username"
MONGO_PASSWORD = "password"
    
""" % name)
    config_file.close()

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
        super( Master, self ).__init__()
        self.id = ObjectId()
        
        self.dictionary = {"key":"value"}
        self.koalalorenzo = "is a great programmer"
        
        self._database = database
        self._collection = "Example"
        
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