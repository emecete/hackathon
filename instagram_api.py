import json
import requests

from utils import get_credentials

HASHTAGS_FILEPATH = 'hashtag.json'


def get_hashtags():
    """
    Read '<HASHTAGS_FILEPATH>' json file
    :return: dictionary with all hashtag file content
    """
    with open(HASHTAGS_FILEPATH) as f:
        return json.load(f)


def get_user_metadata(user_id, params='follower_count,media_count,username'):
    """
    Request uer metadata to Instagram API, for an specific user
    :param user_id: id of an specific Instagram user, from whom it is wanted to know some information
    :param params:  specific fields of information about the user, by default follower_count (user number of followers),
                    media count (number of media in the specifc Instaram account) and username
    :return: dictionary with the specific information required in param 'params' about the user
    """
    response = requests.get(
        ' http://hackathon.ocupa2.com/instagram/%s?fields=%s' % (user_id, params))
    json_data = json.loads(response.text)
    return json_data


class InstagramApiRequests:
    """
    Wrapper class of the Instagram API provided by Ocupa2
    """

    def __init__(self):
        """
        Class initialization; 'token' variable it is needed to make requests
        """
        self.token = get_credentials()['token']

    def get_hashtag_id(self, hashtag):
        response = requests.get(
            ' http://hackathon.ocupa2.com/instagram/ig_hashtag_search?q=%s' % (hashtag))
        json_data = json.loads(response.text)
        return json_data

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

