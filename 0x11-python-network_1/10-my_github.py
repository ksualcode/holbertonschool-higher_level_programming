#!/usr/bin/python3
''' takes in a URL, sends a request to the URL '''

if __name__ == "__main__":
    from requests import get
    from sys import argv

    head = {'Accept': 'application/vnd.github.v3+json'}
    respuesta = get('https://api.github.com/user', auth=(argv[1], argv[2]), headers=head)
    print(respuesta.json().get('id'))
