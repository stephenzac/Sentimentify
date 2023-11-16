import os
import requests
from dotenv import load_dotenv


load_dotenv()
client_secret = os.environ.get("GENIUS_SECRET")
client_id = os.environ.get("GENIUS_CLIENT_ID")


def make_genius_request(endpoint: str, params: dict) -> dict:
    base_url = "https://api.genius.com/" + endpoint
    
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.text)


def search_song(title: str, artist: str) -> dict:
    """
    Use the given song title and artist as search queries
    for the Genius API search endpoint, return the API JSON response
    """
    params = {
        "q": f"{title} {artist}",
        "access_token": "nyUlN2Ic0AqZlc-_5GCKg4AywxbB7ouKlU3cMK_veMa-V3YyJt74zpRxEnOwO2kC"
    }

    response = make_genius_request("search", params)
    return response



if __name__ == "__main__":
    # print(search_song("glimpse", "joji")["response"]["hits"][0]["result"]["path"])
    # make_genius_request({"q": "777 Bruno Mars"})
    for thing in [("777", "bruno mars"), ("the scientist", "coldplay"), ("glimpse", "joji"), ("solar", "lorde"), ("fine by", "grammer")]:
        print(search_song(thing[0], thing[1]))
