#!/usr/bin/python3
''' takes in a URL, sends a request to the URL '''

if __name__ == "__main__":
    from requests import get

    respuesta = get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(respuesta)))
    print("\t- content: {}".format(respuesta))
