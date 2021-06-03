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
        my_dict = dict()
        if (type(attrs) is list and all(type(i) is str for i in attrs)):
            for key in attrs:
                if key in self.__dict__:
                    my_dict.update({key : self.__dict__[key]})
            return my_dict

        return self.__dict__
