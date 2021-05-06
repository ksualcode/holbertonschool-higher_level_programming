#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    add = 0
    div = 0
    for in_list in my_list:
        mul = 1
        for n in range(len(in_list)):
            if n == len(in_list) - 1:
                div += in_list[n]
            mul *= in_list[n]
        add += mul

    return add / div 
