import os
import requests

# either set the GB_API_KEY variable to your API key, or just edit it here
API_KEY = os.getenv("GB_API_KEY", "")

GB_API_BASE = "https://www.giantbomb.com/api"
USER_AGENT = "Tom Nook 3.1 [Nook's Cranny / IE-Compatible]"

def search_games(name):
    url = f"{GB_API_BASE}/games/"
    params = {
        "api_key": API_KEY,
        "format": "json",
        "filter": f"name:{name}",
        "resources": "game"
    }
    headers = {
        "User-Agent": USER_AGENT
    }
    result = requests.get(url, headers = headers, params=params)
    if result.status_code != 200:
        raise Exception(f"something went wrong yo (status = {result.status_code}, body = {result.text})")
    return result.json()["results"]

if __name__ == "__main__":
    results = search_games('animal crossing')
    for result in results:
        print(f"{result['name']} ({result['original_release_date']})")
