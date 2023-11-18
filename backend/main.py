import spotify_api as spotify
import genius_api as genius
import lyrics
import re
import concurrent.futures
from sentiment_analysis import SentimentAnalyzer
from functools import partial


def get_playlist_id(playlist_link: str) -> str:
    """
    Search the given link using a regex for a Spotify
    playlist id. If no ID is found (invalid playlist link),
    return None
    """
    id_regex_pattern = re.compile("playlist\/([a-zA-Z0-9]+)")
    id_match = re.search(id_regex_pattern, playlist_link)

    if id_match:
        return id_match.group(1)
    
    return None


def get_lyrics(item: dict) -> str:
    """
    Search the response from the Genius API for a matching
    song, then get the lyrics from the corresponding lyric page
    """
    try:
        title, artists = spotify.get_title_and_artist(item)
        lyric_search = genius.search_song(title, artists)

        found = False
        for hit in lyric_search["response"]["hits"]:
            for artist in artists:
                if artist.lower() in hit["result"]["primary_artist"]["name"].lower():
                    genius_path = hit["result"]["path"]
                    song_lyrics = lyrics.get_song_lyrics(genius_path)

                    if song_lyrics == None:
                        return None
                    
                    found = True
                    return song_lyrics
            if found:
                found = False
                break
    except (IndexError, TypeError):
        return None


def process_songs(item: dict, sentiment_dict: dict) -> dict:
    """
    Analyze the lyrics and audio features of a track in the playlist
    """

    if item["track"] == None:
        return None

    # Get the song lyrics
    lyrics = get_lyrics(item)

    track_id = item["track"]["id"]
    track_attributes = spotify.get_track_audio_features(track_id)

    if track_attributes == None:
        return None

    sentiment_info_dict = {
        "songName": item["track"]["name"],
        "spotifyDictionary": track_attributes,
        "lyrics": ""
    }

    # Songs without lyrics will be analyzed using just their attributes
    if lyrics != None:
        sentiment_info_dict["lyrics"] = lyrics

    return sentiment_info_dict


def run(playlist_link: str) -> dict:
    """
    The main backend program. Takes a valid Spotify playlist,
    and analyzes each song for an overall mood/sentiment analysis,
    plus an individual analysis for each song
    """

    playlist_id = get_playlist_id(playlist_link)
    playlist_response = spotify.get_playlist_info(playlist_id)

    # Return None to Flask server if invalid playlist/playlist ID
    if playlist_id == None or playlist_response == None:
        return None
    
    playlist_name = playlist_response["name"]
    image_url = playlist_response["images"][0]["url"]

    # Playlist songs
    playlist_songs = spotify.get_playlist_songs(playlist_id)
    track_list = playlist_songs["items"]

    sentiment_dict = SentimentAnalyzer(playlist_name)

    # Process all songs with multiprocessing
    with concurrent.futures.ProcessPoolExecutor() as executor:
        partial_process_songs = partial(process_songs, sentiment_dict=sentiment_dict)
        all_dicts = list(executor.map(partial_process_songs, track_list))
    
    # Use properly returned songs to calculate moods/sentiments
    for info_dict in all_dicts:
        if info_dict != None:
            sentiment_dict.receive_information(info_dict)

    # Do calculations, return final calculated dict attribute
    sentiment_dict.calculate_valence()
    sentiment_dict.calculate_compound_sentiment()
    sentiment_dict.calculate_song_mood()
    sentiment_dict.calculate_song_energy()
    sentiment_dict.calculate_playlist_mood()
    sentiment_dict.calculate_playlist_energy()
    sentiment_dict.calculate_percentages()

    final = sentiment_dict.final_dict
    final["imgURL"] = image_url

    return final
