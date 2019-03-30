import concurrent.futures
import concurrent.futures
import time

from instagram_api import InstagramApiRequests
from rankings import hashtag_to_hashtag_id, get_all_hashtags

ir = InstagramApiRequests()

#hashtag_ids = hashtag_to_hashtag_id(get_all_hashtags())

#ir.get_recent_media(hashtag_id)
#ir.get_post_metadata()


def http_threader(function_name, iterable_list, connections=100):
    out = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=connections) as executor:
        future_to_url = (executor.submit(function_name, element) for element in iterable_list)
        time1 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
            except Exception as exc:
                data = str(type(exc))
            finally:
                out.append(data)

                print("added")
                # print(str(len(out)), end="\r")

        time2 = time.time()
    print(f'Took {time2 - time1:.2f} s')
    return out
