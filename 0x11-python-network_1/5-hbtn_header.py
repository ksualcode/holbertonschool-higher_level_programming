#!/usr/bin/python3
''' takes in a URL, sends a request to the URL '''

if __name__ == "__main__":
    from requests import get, head
    from sys import argv

    respuesta = get(argv[1])
    print(respuesta.headers['X-Request-Id'])
    
