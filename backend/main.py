import spotify_api as spotify
import genius_api as genius
import lyrics
import re
import concurrent.futures
from sentiment_analysis import SentimentAnalyzer



def get_playlist_id(playlist_link: str) -> str:
    """
    Search the given link using regex for a Spotify
    playlist id. If no ID is found (invalid playlist link),
    return None
    """
    id_regex_pattern = r"playlist\/([a-zA-Z0-9]+)"
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
        # song_lyrics = lyrics.get_song_lyrics(lyric_search)

        found = False
        for hit in lyric_search["response"]["hits"]:
            for artist in artists:
                if artist.lower() in hit["result"]["primary_artist"]["name"].lower():
                    genius_path = hit["result"]["path"]
                    song_lyrics = lyrics.get_song_lyrics(genius_path)

                    if song_lyrics == None:
                        # print(f"No lyrics for {title} - {artist}")
                        return None
                    
                    # print(f"Found lyrics for {title} - {artist}")
                    found = True
                    return song_lyrics
            if found:
                found = False
                break
    except (IndexError, TypeError):
        return None


def process_songs(track_list: list) -> dict:
    """
    Go through each song in the playlist and analyze each one
    """
    song_analyzer = SentimentAnalyzer()

    for item in track_list:

        if item["track"] == None:
            continue

        lyrics = get_lyrics(item)

        track_id = item["track"]["id"]
        track_attributes = spotify.get_track_audio_features(track_id)

        # Songs without lyrics will be analyzed using just their attributes
        if lyrics != None:
            print(f"{lyrics}\n----------------------------------------------")
            pass
            # send lyrics to michelle's class
        
    # return song_analyzer.final_dict

        
def run(playlist_link: str) -> dict:
    """
    The backend program
    """
    playlist_id = get_playlist_id(playlist_link)

    # If playlist link is invalid, return None to Flask server
    if playlist_id == None:
        return None
    
    playlist_name = spotify.get_playlist_info(playlist_id)["name"]
    print(f"Playlist name: {playlist_name}")

    playlist_songs = spotify.get_playlist_songs(playlist_id)
    track_list = playlist_songs["items"]

    # calculated_playlist = 

    calculated_playlist = process_songs(track_list)

    return calculated_playlist


"""
const exampleData = {
    "playlist": {
        "GUTS": {
            "mood": "negative", "energy": "high"
        }
    },
    "songs": {
        "Glimpse Of Us": {"mood": "negative", "energy": "low"},
        "Stacy's Mom": {"mood": "positive", "energy": "high"},
        "Locked Out Of Heaven": {"mood": "positive", "energy": "high"},
        "Dandelions": {"mood": "positive", "energy": "medium"},
        "Word Up": {"mood": "neutral", "energy": "medium"},
        "Very long song ": {"mood": "neutral", "energy": "medium"},
        "Bad Romance": {"mood": "neutral", "energy": "high"},

    },
    "moodPercentages": {
        "happy": 0.1,
        "neutral": 0.5,
        "sad": 0.4
    },
    "energyPercentages": {
        "high": 0.4,
        "medium": 0.1,
        "low": 0.5
    }

}
"""
    

if __name__ == "__main__":
    # driving playlist
    # link = "https://open.spotify.com/playlist/0WdmV3JnNihWiaPdi8MBSz"

    # mulan
    # link = "https://open.spotify.com/playlist/4jetnIc7yJLUJsk1okSWMb?si=a4db66966b864daf"

    # public simp playlist lol
    # link = "https://open.spotify.com/playlist/0lgr2ATMsioWvaxYYkn2cD?si=14cf972d327a40c3"

    # bruno mars
    link = "https://open.spotify.com/playlist/6Rxa7PgHtUL9YhmWsl7ZRs?si=505a0f8e95e54c13"

    # instrumental
    # link = "https://open.spotify.com/playlist/67zVq9i2JaNGeigm115kGF?si=c183f943f0c74724"

    run(link)
