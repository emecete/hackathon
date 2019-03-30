import json


def get_credentials():
    with open('user_credentials.json') as f:
        return json.load(f)

