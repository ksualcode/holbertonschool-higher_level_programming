#!/usr/bin/python3
''' Module that contains a class '''


class Student():
    ''' Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Class constructor '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Student class '''
        return (self.__dict__)
