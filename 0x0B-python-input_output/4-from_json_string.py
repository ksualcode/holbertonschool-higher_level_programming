#!/usr/bin/python3
''' Module that contains a function '''
import json


def from_json_string(my_str):
    ''' Function that returns a json in string '''
    return json.loads(my_str)
