from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)

db = client['ocupa2']

def add_post(post_list):
    posts = db.posts
    new_result = posts.insert_many(post_list)
    print('Multiple posts: {0}'.format(new_result.inserted_ids))