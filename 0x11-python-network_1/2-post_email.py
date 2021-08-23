#!/usr/bin/python3
''' takes in a URL, sends a request to the URL '''

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    email = {'email': argv[2]}
    data = parse.urlencode(email)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        respuesta = response.read()
        print(respuesta.decode("utf-8"))
