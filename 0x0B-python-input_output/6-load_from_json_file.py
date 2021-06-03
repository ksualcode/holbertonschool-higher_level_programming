#!/usr/bin/python3
''' Module that contains a function '''
import json


def load_from_json_file(filename):
        ''' Function that puts a json in a file '''
    with open(filename, mode="r", encoding="utf-8") as my_file:
        return(json.load(my_file))
