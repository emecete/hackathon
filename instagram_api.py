import json
from pprint import pprint

import requests

from utils import get_credentials


class ApiRequests:
    def __init__(self):
        self.token = get_credentials()['token']

    def get_hashtag_id(self, hashtag):
        response = requests.get(
            ' http://hackathon.ocupa2.com/instagram/ig_hashtag_search?q=%s&user_id=%s' % (hashtag, self.token))
        json_data = json.loads(response.text)
<<<<<<< Updated upstream
        pprint(json_data)
=======
        return json_data
>>>>>>> Stashed changes

    def get_top_media(self, hashtag_id):
        response = requests.get(
            ' http://hackathon.ocupa2.com/instagram/%d/top_media?&user_id=%s' % (hashtag_id, self.token))
        json_data = json.loads(response.text)
        pprint(json_data)

    def get_recent_media(self, hashtag_id):
        response = requests.get(
            ' http://hackathon.ocupa2.com/instagram/%d/recent_media?&user_id=%s' % (hashtag_id, self.token))
        json_data = json.loads(response.text)
        pprint(json_data)

    def get_post_metadata(self, post_id, id=True, comments_count=True):
        response = requests.get(
            ' http://hackathon.ocupa2.com/instagram/media/%d?fields={fields}' % (post_id, ))
        json_data = json.loads(response.text)
        pprint(json_data)