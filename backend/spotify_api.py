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
        print(response.text)


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


def get_title_and_artist(song_id: str) -> (str, str):
    """
    Given a song ID, extract the song title and artist from
    the track data returned by the Spotify API
    """

    endpoint = f"tracks/{song_id}"
    song_info = make_spotify_request(endpoint)
    return (song_info["name"], song_info["artists"][0]["name"])


def get_playlist_songs(playlist_id: str) -> list:
    """
    Given a playlist ID, make a request to the Spotify API
    to get an object containing the songs of the playlist,
    and return a list of the names of every song in the playlist
    """
    endpoint = f"playlists/{playlist_id}/tracks"
    response = make_spotify_request(endpoint)
    songs_list = [song["track"] for song in response["items"]]
    return songs_list


def get_track_audio_features(song_id: str) -> dict:
    """
    Given a song ID, make a request to the Spotify API for
    an object containing the audio features of a song
    """
    endpoint = f"audio-features/{song_id}"
    response = make_spotify_request(endpoint)
    return response
