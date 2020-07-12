import requests
from requests.exceptions import Timeout


DOMAIN_URL = "https://www.googleapis.com/customsearch/v1?"


def google_search(keyword):
    retry = 0
    while retry < 3:
        try:
            res = requests.get(DOMAIN_URL,
                               params={
                                   'key': 'AIzaSyA4yZTbZzMlwnjnAXNdhJxekwvc7-6Maus',
                                   'cx': '000106981491294653254:5m1wlreuqrq',
                                   'q': keyword
                               },
                               timeout=2)
            response = res.json()
            parsed_urls = list(map(lambda x: x['link'], response['items']))
            return parsed_urls
        except Timeout as e:
            print("retrying")
            retry += 1
            continue
    return []


if __name__ == '__main__':
    keyword = "lectures"
    google_search(keyword)
