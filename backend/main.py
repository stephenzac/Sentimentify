import spotify_api
import genius_api
import lyrics


def get_playlist_id(playlist_link: str) -> str:
    # driving playlist
    # https://open.spotify.com/playlist/0WdmV3JnNihWiaPdi8MBSz

    # mulan
    # https://open.spotify.com/playlist/4jetnIc7yJLUJsk1okSWMb?si=a4db66966b864daf

    # https://open.spotify.com/playlist/0lgr2ATMsioWvaxYYkn2cD?si=14cf972d327a40c3

    playlist_id = "0lgr2ATMsioWvaxYYkn2cD"
    return playlist_id


def process_songs(playlist_songs: dict) -> list:
    for item in playlist_songs["items"]:
        if item["track"] == None:
            continue
        title, artist = spotify_api.get_title_and_artist(item)
        lyric_search = genius_api.search_song(title, artist)
        print(lyric_search["response"]["hits"][0]["result"]["path"])
    

def run(playlist_link: str) -> dict:
    playlist_id = get_playlist_id(playlist_link)
    playlist_songs = spotify_api.get_playlist_songs(playlist_id)

    # If the playlist link is invalid, return None to Flask server
    if playlist_songs == None:
        print("Correct.")
        return None
    
    process_songs(playlist_songs)

    return None
    



if __name__ == "__main__":
    run("https://open.spotify.com/playlist/4jetnIc7yJLUJsk1okSWMb?si=a4db66966b864daf")
