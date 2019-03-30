from pprint import pprint

from instagram_api import get_hashtags, InstagramApiRequests


def get_all_hashtags():
    hashtags = list()
    json_hashtags = get_hashtags()
    for hashtag_group in json_hashtags:
        for hashtag in json_hashtags[hashtag_group]:
            hashtags.append(hashtag.replace("#", ""))
    return hashtags


def hashtag_to_hashtag_id(hashtag_list):
    hashtag_id_list = []
    for h in hashtag_list:
        hashtag_id_list = InstagramApiRequests.get_hashtag_id(h)
    return hashtag_id_list


def get_all_posts():
    ir = InstagramApiRequests()
    for hashtag in get_all_hashtags():
        pprint(ir.get_recent_media(ir.get_hashtag_id(hashtag)['id']))

get_all_posts()
