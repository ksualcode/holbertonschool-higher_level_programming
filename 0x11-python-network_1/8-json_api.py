#!/usr/bin/python3
''' takes in a URL, sends a request to the URL '''

if __name__ == "__main__":
    from requests import post, exceptions
    from sys import argv

    if (len(argv) == 2):
        chara = argv[1]
    else:
        chara = ""

    respuesta = post('http://0.0.0.0:5000/search_user', {'q': chara})
    try:
        resp_json = respuesta.json()
        id = resp_json.get('id')
        name = resp_json.get('name')

        if (len(resp_json) == 0 or id is None or name is None):
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception as e:
        print("Not a valid JSON")
