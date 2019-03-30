import pandas as pd
import concurrent.futures
import requests
import time
import asyncio

from instagram_api import get_user_metadata, InstagramApiRequests
from rankings import hashtag_to_hashtag_id, get_all_hashtags

ir = InstagramApiRequests()
#out = []
CONNECTIONS = 100
TIMEOUT = 5

hashtag_ids = hashtag_to_hashtag_id(get_all_hashtags())


def load_url_get_recent_media(hashtag_id):
    ans = ir.get_recent_media(hashtag_id)
    return ans


# with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
#     future_to_url = (executor.submit(load_url_get_recent_media, hashtag_id) for hashtag_id in hashtag_ids)
#     time1 = time.time()
#     for future in concurrent.futures.as_completed(future_to_url):
#         try:
#             data = future.result()
#         except Exception as exc:
#             data = str(type(exc))
#         finally:
#             #out.append(data)
#             print("added")
#             #print(str(len(out)), end="\r")
#
#     time2 = time.time()

# print(f'Took {time2 - time1:.2f} s')
#print(pd.Series(out).value_counts())

