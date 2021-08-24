#!/usr/bin/python3
''' takes in a URL, sends a request to the URL '''

if __name__ == "__main__":
    from requests import get
    from sys import argv

    respuesta = get(argv[1])
    if (respuesta.status_code <= 400):
        print(respuesta.text)
    else:
        print("Error code: " + str(respuesta.status_code))
