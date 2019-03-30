from pprint import pprint

from instagram_api import get_hashtags, InstagramApiRequests


def get_all_hashtags():
    hashtags = list()
    json_hashtags = get_hashtags()
    for hashtag_group in json_hashtags:
        for hashtag in json_hashtags[hashtag_group]:
            hashtags.append(hashtag)

    return hashtags

def get_all_posts():
    ir = InstagramApiRequests()
    for hashtag in get_all_hashtags():
        pprint(ir.get_recent_media(ir.get_hashtag_id(hashtag)['id']))

get_all_posts()
