from pymongo import MongoClient


class mongo_db:
    def __init__(self):
        client = MongoClient('localhost', 32768)
        self.db = client['ocupa2']

    def add_posts(self, post_list):
        posts = self.db.posts
        new_result = posts.insert_many(post_list)
        print('Multiple posts: {0}'.format(new_result.inserted_ids))

    def add_post(self, post):
        posts = self.db.posts
        result = posts.insert_one(post)
        print('Post: {0}'.format(result.inserted_id))