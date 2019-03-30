import json
import requests

from utils import get_credentials

HASHTAGS_FILEPATH = 'hashtag.json'


def get_hashtags():
    with open(HASHTAGS_FILEPATH) as f:
        return json.load(f)


def get_user_metadata(user_id, params='follower_count,media_count,username'):
    response = requests.get(
        ' http://hackathon.ocupa2.com/instagram/%s?fields=%s' % (user_id, params))
    json_data = json.loads(response.text)
    return json_data


class InstagramApiRequests:
    def __init__(self):
        self.token = get_credentials()['token']

    def get_hashtag_id(self, hashtag):
        response = requests.get(
            ' http://hackathon.ocupa2.com/instagram/ig_hashtag_search?q=%s&user_id=%s' % (hashtag, self.token))
        json_data = json.loads(response.text)
        return (json_data)

    def get_top_media(self, hashtag_id):
        response = requests.get(
            ' http://hackathon.ocupa2.com/instagram/%d/top_media?&user_id=%s' % (hashtag_id, self.token))
        json_data = json.loads(response.text)
        return (json_data)

    def get_recent_media(self, hashtag_id):
        response = requests.get(
            ' http://hackathon.ocupa2.com/instagram/%d/recent_media?&user_id=%s' % (hashtag_id, self.token))
        json_data = json.loads(response.text)
        return (json_data)

    def get_post_metadata(self, post_id, params='username'):
        response = requests.get(
            ' http://hackathon.ocupa2.com/instagram/media/%d?fields=%s' % (post_id,params))
        json_data = json.loads(response.text)
        return json_data

