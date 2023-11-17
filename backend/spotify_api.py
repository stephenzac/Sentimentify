import os
import requests
from dotenv import load_dotenv

load_dotenv()
client_secret = os.environ.get("SPOTIFY_SECRET")
client_id = os.environ.get("SPOTIFY_CLIENT_ID")


def make_spotify_request(endpoint: str) -> dict:
    """
    Make a request to the Spotify API at the given endpoint,
    and return the response as a JSON object
    """
    request_url = "https://api.spotify.com/v1/" + endpoint
    access_token = get_spotify_auth_token()
    headers = {
        "Content-Type":"application/x-www-form-urlencoded",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(request_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"{response.text}")


def get_spotify_auth_token() -> str:
    """
    Get an authorization token using client ID and secret
    to make calls to the Spotify API
    """

    post_url = "https://accounts.spotify.com/api/token"

    data = {
        "grant_type": "client_credentials",
        "client_secret": client_secret,
        "client_id": client_id
    }

    response = requests.post(post_url, data=data)

    if response.status_code == 200:
        access_token = response.json()["access_token"]
        return access_token
    else:
        print(response.text)


def get_title_and_artist(playlist_item: dict) -> (str, [str]):
    """
    Given a playlist item (song), extract and return
    a tuple of the name of the song and the artist
    """

    return ((playlist_item["track"]["name"], [artist["name"] for artist in playlist_item["track"]["artists"]]))


def get_playlist_songs(playlist_id: str) -> list:
    """
    Given a playlist ID, make a request to the Spotify API
    to get and return an object containing the songs of the playlist
    """
    endpoint = f"playlists/{playlist_id}/tracks"

    response = make_spotify_request(endpoint)

    if response == None:
        return None
    
    return response


def get_playlist_info(playlist_id: str) -> dict:
    """
    Given a playlist ID, make a request to the Spotify API
    to get and return an object containing a playlist's details
    """
    endpoint = f"playlists/{playlist_id}"

    response = make_spotify_request(endpoint)

    if response == None:
        return None
    
    return response


def get_track_audio_features(song_id: str) -> dict:
    """
    Given a song ID, make a request to the Spotify API for
    an object containing the audio features of a song
    """
    endpoint = f"audio-features/{song_id}"
    response = make_spotify_request(endpoint)
    return response


def get_multiple_audio_features(ids: str) -> dict:
    endpoint = "audio-features?ids="
    endpoint += requests.utils.quote(ids)
    print(endpoint)

    response = make_spotify_request(endpoint)
    return response
