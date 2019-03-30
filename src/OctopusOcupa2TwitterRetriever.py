from src.TwitterRetriever import TwitterRetriever
import json
from octopus import Octopus


class OctopusOcupa2TwitterRetriever(TwitterRetriever):
    
    def __init__(self, httpClient : Octopus):
        self.httpClient = httpClient
    
    def postsOfHashtags(self, hashtags: list) -> list:
        data = {}

        def handle_url_response(url, response, hashtag):
            if 200 != response.status:
                data.update(hashtag, [])
            else:
                parsed_response = json.loads(response.text)
                data.update(hashtag, parsed_response['data'])

        for hashtag in hashtags:
            self.httpClient.enqueue(
                url='http://hackathon.ocupa2.com/twitter/1.1/tweets.json?q=' + hashtag, 
                handler=handle_url_response, 
                hashtag=hashtag)

        self.httpClient.wait()

        return data
