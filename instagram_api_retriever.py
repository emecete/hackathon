import aiohttp
import asyncio
import json
from pprint import pprint


async def fetch(url, session = None):
    async def wrapped(session):
        async with session.get(url) as response:
            return await response.text()
    
    if session == None:
        async with aiohttp.ClientSession() as session:
            return await wrapped(session)
    else: return await wrapped(session)


async def get_hashtag_id(hashtag):
    response = await fetch('http://hackathon.ocupa2.com/instagram/ig_hashtag_search?q=%s' % hashtag)
    json_data = json.loads(response)
    return json_data['id']


async def get_recent_media(hashtag_id):
    response = await fetch('http://hackathon.ocupa2.com/instagram/%s/recent_media' % hashtag_id)
    json_data = json.loads(response)
    return json_data['data']


async def get_post_metadata(post_id, params='username'):
    response = await fetch('http://hackathon.ocupa2.com/instagram/media/%s?fields=%s' % (post_id, params))
    json_data = json.loads(response)
    return json_data[0]


async def get_user_metadata(user_id, params='follower_count,media_count,username'):
    response = await fetch('http://hackathon.ocupa2.com/instagram/%s?fields=%s' % (user_id, params))
    json_data = json.loads(response)[0]
    json_data.update({'user_id': user_id})
    return json_data


async def main(hashtags):
    users = {}
    all_posts = {}
    for hashtag in hashtags:
        hashtag = hashtag[1:]
        print(hashtag)
        hashtagid = await get_hashtag_id(hashtag)
        recent_media = await get_recent_media(hashtagid)
        for post in recent_media:
            maybe_post = all_posts.get(post['id'], None)
            if not maybe_post:
                post_metadata = await get_post_metadata(post['id'])
                if not users.get(post_metadata['userId'], None):
                    usermetadata = await get_user_metadata(post_metadata['userId'])
                    users[post_metadata['userId']] = usermetadata
                post.update({
                    "user": users[post_metadata['userId']],
                    "hashtags": [hashtag]})
            else:
                maybe_post["hashtags"].append(hashtag)
                post = maybe_post
            all_posts[post['id']] = post
    with open("/home/sosa/Escritorio/data2.json", "w") as file:
        file.write(json.dumps(list(all_posts.values())))


if __name__ == '__main__':
    hashtags = []
    with open("/home/sosa/Escritorio/hashtag.json") as file:
        parsed_data = json.loads(file.read())
        for hashtag_group in parsed_data.keys():
            hashtags += parsed_data[hashtag_group]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(hashtags))