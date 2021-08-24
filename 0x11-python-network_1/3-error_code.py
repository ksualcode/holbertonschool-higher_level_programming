#!/usr/bin/python3
''' takes in a URL, sends a request to the URL '''

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except error.URLError as e:
        print("Error code: " + str(e.code))
