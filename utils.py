import json


def get_credentials():
    with open('user_credentials.json') as f:
        return json.load(f)


def get_meta_hashtags():
    with open('hashtag.json') as f:
        return (meta for meta in json.load(f))



