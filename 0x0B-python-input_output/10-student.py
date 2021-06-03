#!/usr/bin/python3
''' Module that contains a class '''


class Student():
    ''' Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Class constructor '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Student class '''
        my_dict = self.__dict__
        if (type(attrs) == "list" and all(type(i) is str for i in attrs)):
            for key in attrs:
                if (key != d_key for d_key in my_dict):
                    my_dict.pop(key)
        
        return my_dict
