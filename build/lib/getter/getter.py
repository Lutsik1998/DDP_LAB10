import requests


def get_author_entries(key, pk):
    link = 'https://api.e-science.pl/api/azon/authors/entries/' + str(pk) + '/'
    try:
        return requests.get(link, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e

def get_laboratories(key):
    url = 'https://api.e-science.pl/api/azon/databases/elaboratory/'
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e

