import json
from pprint import pprint

import requests

from utils import get_credentials


class ApiRequests:
    def __init__(self):
        self.token = get_credentials()['token']

    def get_top_media(self, hashtag_id):
        response = requests.get(
            ' http://hackathon.ocupa2.com/instagram/%d/top_media?&user_id=%s' % (hashtag_id, self.token))
        json_data = json.loads(response.text)
        pprint(json_data)
