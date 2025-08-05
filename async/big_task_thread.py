import time
from concurrent.futures import ProcessPoolExecutor

import requests


def fetch_url_data(pg_url):
    """get a url page

    Args:
        pg_url: url to fetch

    return: url page
    """
    try:
        resp = requests.get(pg_url)
    except Exception as e:
        print(f"Error occured during fetch data from url{pg_url}")
    else:
        return resp.content


def get_all_url_data(url_list):
    """get a list of urls and get its pages

    Args:
        url_list: a list of urls
    return: list of url pages
    """
    with ProcessPoolExecutor() as executor:
        resp = executor.map(
            fetch_url_data, url_list
        )  # run the function fetch_url_data on the url's list
    return resp


if __name__ == "__main__":
    url = "https://www.velotio.com/careers"
    for ntimes in [1, 10, 50, 100, 500]:  # get the url in several different cuentety
        start_time = time.time()
        responses = get_all_url_data(
            [url] * ntimes
        )  # call the function several number of times
        print(
            f"Fetch total {ntimes} urls and process takes {time.time() - start_time} seconds"
        )
