import requests

def get_entries_page(key, page=0):
    link = 'https://api.e-science.pl/api/azon/entry/filter/?limit=100&offset=' + str(page) +'00'
    try:
        return requests.get(link, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e

def get_programming_languages(key):
    link = 'https://api.e-science.pl/api/azon/programminglanguages/'
    try:
        return requests.get(link, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return
