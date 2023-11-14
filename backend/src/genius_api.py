import os
import requests
from dotenv import load_dotenv


load_dotenv()
genius_api_key = os.environ.get("GENIUS_API_KEY")


def make_genius_request(song_title: str, artist: str):
    base_url = "https://api.genius.com/search"
    headers = {
        "Authorization": f"Bearer {genius_api_key}"
    }
    params = {
        "q": f"{song_title} {artist}"
    }

    response = requests.get(base_url, headers, params)

    if response.status_code == 200:
        data = response.json()

    return data
