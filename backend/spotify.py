from spotify_api import make_spotify_request


def get_playlist_items(playlist_id: str) -> list:
    """
    
    """
    
    endpoint = f"playlists/{playlist_id}/tracks"
    songs_list = make_spotify_request(endpoint)


def get_title_and_artist(song_id: str) -> (str, str):
    """
    
    """

    endpoint = f"tracks/{song_id}"
    song_info = make_spotify_request(endpoint)
    return (song_info["name"], song_info["artists"][0]["name"])


def get_audio_features(song_id: str) -> dict:
    """
    
    """

    endpoint = f"audio-features/{song_id}"
    audio_features = make_spotify_request(endpoint)
    return audio_features


if __name__ == "__main__":
    print(get_title_and_artist("f76ef63dc4fe4787"))
