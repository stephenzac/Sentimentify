import os
import requests
import urllib
from dotenv import load_dotenv


load_dotenv()
client_secret = os.environ.get("GENIUS_SECRET")
client_id = os.environ.get("GENIUS_CLIENT_ID")


def make_genius_request(endpoint: str, params: dict):
    base_url = "https://api.genius.com/" + endpoint
    
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    else:
        print(response.text)


# def get_genius_auth_token() -> str:
#     """
#     Get an authorization token using client ID and secret
#     to make calls to the Spotify API
#     """
#     redirect_url = "https://api.genius.com/oauth/authorize?"
#     params = {
#         "client_id": "Oqvl_30Tx8m4hgDJ2PebI3jbdxenFeLg6KMHa1HsFR_LWgcOrZTwynSn6B4lidvQ",
#         "redirect_uri": "http://127.0.0.1:5000",
#         "scope": "me",
#         "response_type": "code"
#     }
#     redirect_url += urllib.parse.urlencode(params)


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
    print(search_song("777", "Bruno Mars"))
    # make_genius_request({"q": "777 Bruno Mars"})
