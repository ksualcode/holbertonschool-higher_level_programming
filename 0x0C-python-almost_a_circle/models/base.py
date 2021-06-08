#!/usr/bin/python3
''' Module with a base class '''
import json
import os


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
        mlist = "[]"
        if list_objs is not None:
            mlist = cls.to_json_string([o.to_dictionary() for o in list_objs])

        with open("{}.json".format(cls.__name__), 'w') as file:
            file.write(mlist)

    @staticmethod
    def from_json_string(json_string):
        ''' Converts a JSON stringt representation to List '''
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Creates an instance '''
        this_class = cls.__name__
        if this_class == 'Square':
            this_instance = cls(69)
        elif this_class == 'Rectangle':
            this_instance = cls(69, 420)
        this_instance.update(**dictionary)
        return this_instance

    @classmethod
    def load_from_file(cls):
        ''' Returns list of instances '''
        my_list = []
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return my_list

        with open(filename, "r") as my_file:
            for i in cls.from_json_string(my_file.read()):
                my_list.append(cls.create(**i))

        return my_list
