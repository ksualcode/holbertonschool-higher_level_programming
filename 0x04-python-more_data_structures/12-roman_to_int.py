#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or None:
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = roman_string
    n = 0
    for i in range(len(r)):
        if r[i] in rom_n:
            if i != len(r) - 1:
                if rom_n[r[i]] < rom_n[r[i + 1]]:
                    n -= rom_n[r[i]]
                    continue
            n += (rom_n[r[i]])

    return n
