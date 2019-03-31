import concurrent.futures
import concurrent.futures
import time


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
        time2 = time.time()
    print(f'Took {time2 - time1:.2f} s')
    return out
