#!/usr/bin/python3
''' script that fetches https://intranet.hbtn.io/status '''

if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        respuesta = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(respuesta)))
        print("\t- content: {}".format(respuesta))
        print("\t- utf8 content: {}".format(respuesta.decode("utf-8")))
