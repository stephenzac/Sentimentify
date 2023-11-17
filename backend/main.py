import spotify_api as spotify
import genius_api as genius
import lyrics
import re
import concurrent.futures
from sentiment_analysis import SentimentAnalyzer
from functools import partial


def get_playlist_id(playlist_link: str) -> str:
    """
    Search the given link using regex for a Spotify
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
    Search the Genius search response for a matching
    song, then get the lyrics from the lyric page
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
    The main backend program
    """

    playlist_id = get_playlist_id(playlist_link)

    # If playlist link is invalid, return None to Flask server
    if playlist_id == None:
        return None
    
    playlist_response = spotify.get_playlist_info(playlist_id)

    if playlist_response == None:
        return None
    
    playlist_name = playlist_response["name"]

    # Playlist songs
    playlist_songs = spotify.get_playlist_songs(playlist_id)
    track_list = playlist_songs["items"]

    sentiment_dict = SentimentAnalyzer(playlist_name)

    # Process all songs with multiprocessing
    with concurrent.futures.ProcessPoolExecutor() as executor:
        partial_process_songs = partial(process_songs, sentiment_dict=sentiment_dict)
        all_dicts = list(executor.map(partial_process_songs, track_list))
    
    for info_dict in all_dicts:
        if info_dict != None:
            sentiment_dict.receive_information(info_dict)

    sentiment_dict.calculate_valence()
    sentiment_dict.calculate_compound_sentiment()
    sentiment_dict.calculate_song_mood()
    sentiment_dict.calculate_song_energy()
    sentiment_dict.calculate_playlist_mood()
    sentiment_dict.calculate_playlist_energy()
    sentiment_dict.calculate_percentages()
    return sentiment_dict.final_dict


if __name__ == "__main__":
    # driving playlist
    # link = "https://open.spotify.com/playlist/0WdmV3JnNihWiaPdi8MBSz"

    # mulan
    link = "https://open.spotify.com/playlist/4jetnIc7yJLUJsk1okSWMb?si=a4db66966b864daf"

    # public simp playlist lol
    # link = "https://open.spotify.com/playlist/0lgr2ATMsioWvaxYYkn2cD?si=14cf972d327a40c3"

    # bruno mars
    # link = "https://open.spotify.com/playlist/6Rxa7PgHtUL9YhmWsl7ZRs?si=505a0f8e95e54c13"

    # instrumental
    # link = "https://open.spotify.com/playlist/67zVq9i2JaNGeigm115kGF?si=c183f943f0c74724"

    # skyrim
    # link = "https://open.spotify.com/playlist/1ANRT7IOKu6PqW7TI5JFcs?si=588f923ba3f04a12"

    # ids = "2ALh2jqA7KldpHMUHvRomw,2NqyjfDXy0XfXCSPXMsKzi,"
    # print(spotify.get_track_audio_features("5OEXISM55Inhcs4Ea29Iej"))

    print(run(link))
