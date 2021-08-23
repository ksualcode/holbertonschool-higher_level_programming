#!/usr/bin/python3
''' takes in a URL, sends a request to the URL '''

if __name__ == "__main__":
    from urllib import request, response
    from sys import argv

    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        respuesta = response.info()
        print(respuesta["X-Request-Id"])
