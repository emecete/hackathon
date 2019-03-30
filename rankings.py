from pprint import pprint

from instagram_api import get_hashtags, InstagramApiRequests, get_user_metadata
from mongodb.utils import mongo_db


def get_all_hashtags():
    """
    Read the 'hashtag.json' file, in which it is contained different hashtags for different influencer types
    :return: A list containing all hashtags without '#' symbol
    """
    hashtags = list()
    json_hashtags = get_hashtags()
    for hashtag_group in json_hashtags:
        for hashtag in json_hashtags[hashtag_group]:
            hashtags.append(hashtag.replace("#", ""))
    return hashtags


def hashtag_to_hashtag_id(hashtag_list):
    """
    Request to Instagram API in order to obtain the hashtag_id for each of them (hashtag_list)
    :param hashtag_list: List of strings, hashtag names
    :return: A list of ids corresponding to Instagram hashtags
    """
    hashtag_id_list = []
    for h in hashtag_list:
        hashtag_id_list = InstagramApiRequests.get_hashtag_id(h)
    return hashtag_id_list


def get_all_posts():
    """

    :return:
    """
    mdb = mongo_db()
    ir = InstagramApiRequests()
    for hashtag in get_all_hashtags():
        posts = ir.get_recent_media(ir.get_hashtag_id(hashtag)['id'])['data']
        for post in posts:
            user = ir.get_post_metadata(post['id'])[0]['userId']
            post['user'] = get_user_metadata(user)[0]
            mdb.add_post(post)


get_all_posts()
