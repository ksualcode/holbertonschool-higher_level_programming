#!/usr/bin/python3
''' Module that contains a function '''
from json import encoder
from sys import argv
from os import path
save_json_file = __import__('5-save_to_json_file').save_to_json_file
load_json_file = __import__('6-load_from_json_file').load_from_json_file


if path.exists("add_item.json"):
    my_file = load_json_file("add_item.json")
            
else:
    my_file = []

for i in range(1, len(argv)):
    my_file.append(argv[i])

save_json_file(my_file, "add_item.json")
