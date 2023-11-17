import os
import requests
from dotenv import load_dotenv


load_dotenv()
client_secret = os.environ.get("GENIUS_SECRET")
client_id = os.environ.get("GENIUS_CLIENT_ID")


def make_genius_request(endpoint: str, params: dict) -> dict:
    """
    Given an endpoint and query paramters, call the
    Genius API at the given endpoint and 
    return the response as a JSON object
    """
    base_url = "https://api.genius.com/" + endpoint
    
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"{response.text}")


def search_song(title: str, artist: str) -> dict:
    """
    Use the given song title and artist as search queries
    for the Genius API search endpoint, return the API JSON response
    """
    params = {
        "q": f"{title} - {artist}",
        "access_token": "nyUlN2Ic0AqZlc-_5GCKg4AywxbB7ouKlU3cMK_veMa-V3YyJt74zpRxEnOwO2kC"
    }

    response = make_genius_request("search", params)
    return response
