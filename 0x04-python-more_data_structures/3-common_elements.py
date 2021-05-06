#!/usr/bin/python3
def common_elements(set_1, set_2):
    # new_list = list(filter(lambda x: x in set_2, set_1))
    new_list = list(set(set_1) & set(set_2))
    return new_list
