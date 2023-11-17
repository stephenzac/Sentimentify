import requests
from bs4 import BeautifulSoup


def get_song_lyrics(genius_endpoint: str) -> str:
    """
    Get the lyrics of a song by using BeautifulSoup
    to web scrape a genius.com page
    """
    url = "https://genius.com" + genius_endpoint
    page = requests.get(url)
    html = BeautifulSoup(page.content, "html.parser")
    lyrics_element = html.find("div", {"data-lyrics-container": "true"})
    
    if lyrics_element:
        lyrics = lyrics_element.get_text()
        return lyrics
    else:
        return None
