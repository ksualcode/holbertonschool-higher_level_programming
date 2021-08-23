#!/usr/bin/python3
''' script that fetches https://intranet.hbtn.io/status '''
from urllib import request

with request.urlopen('https://intranet.hbtn.io/status') as response:
    respuesta = response.read()
    print("Body response:")
    print("\t- type: {}".format(respuesta))
    print("\t- content: {}".format(type(respuesta)))
    print("\t- utf8 content: {}".format(respuesta.decode("utf-8")))
