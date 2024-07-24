# Sentimentify

## 📖 What is Sentimentify?
Sentimentify is a web application built by Michelle Lee, Stanley Liu, and Stephen Zacarias for ICSSC's week-long 2023 WebJam.
It gives users insight into the mood and energy of the music they listen to. Users will input a Spotify playlist link, and receive calculated 
sentiment, mood, and energy scores for the overall playlist, as well as for each individual song. 

## ⚙️ How it works
The React + Vite frontend will send a playlist to the backend through a POST request to the Python Flask server. After verifying the
validity of the playlist link, various calls are made to the Spotify and Genius APIs using multiprocessing to quickly retrieve information about each song in the
playlist. Genius web pages are also scraped using Beautiful Soup for song lyrics. This song information is passed to a module that
performs sentiment analysis on the lyrics, weighs the sentiment scores, and combines them with the audio feature scores provided by
the Spotify API. After performing calculations of the songs' sentiments/energies/moods, this information is sent to the frontend back through
the Flask server, and displayed to the user.

## 🧠 Challenges we ran into
* Making API calls for Genius webpages and Spotify track attributes really slowed the program down. However, adding multiprocessing
to make parallel API calls drastically sped up execution of the application.
* Dealing with unexpected behaviors like API calls that returned
errors, or unexpected return values from these calls was difficult to deal with, but by testing different playlists of varying lengths and
song types, we were able to test for different kinds of program behavior. 
