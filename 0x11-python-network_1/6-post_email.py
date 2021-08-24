#!/usr/bin/python3
''' takes in a URL, sends a request to the URL '''

if __name__ == "__main__":
    from requests import post
    from sys import argv

    respuesta = post(argv[1], {'email': argv[2]})
    print(respuesta.text)
