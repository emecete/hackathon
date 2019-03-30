from pprint import pprint

from instagram_api import get_hashtags, InstagramApiRequests, get_user_metadata
from mongodb.utils import mongo_db


def get_all_hashtags():
    hashtags = list()
    json_hashtags = get_hashtags()
    for hashtag_group in json_hashtags:
        for hashtag in json_hashtags[hashtag_group]:
            hashtags.append(hashtag.replace("#", ""))
    return hashtags


async def hashtag_to_hashtag_id(hashtag_list):
    ir = InstagramApiRequests()
    hashtag_id_list = []
    for h in hashtag_list:
        print(h)
        hashtag_id_list.append(await ir.get_hashtag_id(h)['id'])
    return hashtag_id_list


def get_all_posts():
    mdb = mongo_db()
    ir = InstagramApiRequests()
    for hashtag in get_all_hashtags():
        posts = ir.get_recent_media(ir.get_hashtag_id(hashtag)['id'])['data']
        for post in posts:
            user = ir.get_post_metadata(post['id'])[0]['userId']
            post['user'] = get_user_metadata(user)[0]
            mdb.add_post(post)

