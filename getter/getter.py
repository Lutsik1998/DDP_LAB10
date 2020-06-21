import requests



def get_research_centers(key):
    link = 'https://api.e-science.pl/api/azon/databases/pwr_research_centers/'
    try:
        return requests.get(link, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e

def get_databases(key):
    url = 'https://api.e-science.pl/api/azon/databases/'
    try:
        return requests.get(url, headers={'X-Api-Key': key}).json()['results']
    except Exception as e:
        return e