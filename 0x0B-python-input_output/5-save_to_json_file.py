#!/usr/bin/python3
''' Module that contains a function '''
import json


def save_to_json_file(my_obj, filename):
    ''' Function that puts a json in a file '''
    with open(filename, mode="w+", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
