import pandas as pd
import concurrent.futures
import requests
import time

from rankings import hashtag_to_hashtag_id, get_all_hashtags

out = []
CONNECTIONS = 100
TIMEOUT = 5

hashtag_ids = hashtag_to_hashtag_id(get_all_hashtags())
urls =

def load_url(url, timeout):
    ans = requests.head(url, timeout=timeout)
    return ans.status_code

with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = (executor.submit(load_url, url, TIMEOUT) for url in urls)
    time1 = time.time()
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data = future.result()
        except Exception as exc:
            data = str(type(exc))
        finally:
            out.append(data)

            print(str(len(out)),end="\r")

    time2 = time.time()

print(f'Took {time2-time1:.2f} s')
print(pd.Series(out).value_counts())