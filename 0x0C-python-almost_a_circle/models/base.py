#!/usr/bin/python3
''' Module with a base class '''

import json

class Base():
    ''' Superclass for other classes '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' Class constructor '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns a json string representation '''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Writes a JSON file '''
        my_list = {}
        if list_objs is not None:
            my_list = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open("{}.json".format(cls.__name__), 'w') as file:
            file.write(my_list)
