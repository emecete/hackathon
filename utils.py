import json


def get_credentials():
    """
    Read the file 'user_credentials.json' in which there is information about the developer user (api key and email)
    :return: dictionary with 'user_credentials.json' content
    """
    with open('user_credentials.json') as f:
        return json.load(f)


