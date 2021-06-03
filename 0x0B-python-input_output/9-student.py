#!/usr/bin/python3
''' Module that contains a class '''
class_to_json = __import__('8-class_to_json').class_to_json


class Student():
    ''' Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Class constructor '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Student class '''
        return class_to_json(self)
