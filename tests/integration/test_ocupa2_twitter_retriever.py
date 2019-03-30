from src import OctopusOcupa2TwitterRetriever
from octopus import Octopus

class TestOcupa2TwitterRetriever:
    def test_one(self):
        twr_client = OctopusOcupa2TwitterRetriever(Octopus(
            concurrency=4, auto_start=True, cache=True,
            expiration_in_seconds=10
        ))
        posts = twr_client.postsOfHashtags(['gethealthy'])
        print(posts)