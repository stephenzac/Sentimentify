from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:

    def __init__(self):
        """
        final_dict is a dictionary in the format 
        {
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

        lyrics is a dictionary with the song title as the key and a string as the item {song_title : "lyrics"}
        dictionary is the received Spotify dictionary
        vader is the sentiment analyzer object
        song_mood_stats is a dictionary {song_title : (valence, vader_sentiment)}
        """

        self.final_dict = {"playlist" : {}, "songs" : {}, "moodPercentages" : {}, "energyPercentages" : {}}
        self.lyrics = {}
        self.spotify_dictionary = {}
        self.vader = SentimentIntensityAnalyzer()

        self.song_mood_stats = {}


    #receive lyrics
    def receive_lyrics(self, lyrics):
        self.lyrics = lyrics


    #receive Spotify dictionary
    def receive_dictionary(self, dictionary):
        self.spotify_dictionary = dictionary
        for song in self.spotify_dictionary:
            self.final_dict[song] = {}


    #add valence to song_stats in -1 to 1 scale
    def calculate_valence(self):

        for song in self.spotify_dictionary:
            self.song_mood_stats[song][0] = self.spotify_dictionary["audio_features"][0]["valence"]


    #calculate sentiment analysis of a song's lyrics
    #Do it line by line?
    def calculate_compound_sentiment(self):

        for song in self.lyrics:
            self.song_mood_stats[song][1] = self.vader.polarity_scores(self.lyrics[song])['compound'] * 0.5 + 0.5

        #or
        for song in self.lyrics:
            sentiment = 0
            numLines = 0
            lines = self.lyrics[song].split('.')

            for line in lines:
                sentiment += self.vader.polarity_scores(line)["compound"]
                numLines += 1
            
            self.song_mood_stats[song][1] = sentiment / numLines
                


    #use compound sentiment and valence to calculate total mood
    def calculate_song_mood(self):
        for song in self.song_mood_stats:
            mood = (self.song_mood_stats[song][0] * 0.6) + (self.song_mood_stats[song][1] * 0.4)
            if mood <= 0.33:
                self.final_dict["songs"]["mood"] = "negative"
            elif mood >= 0.66:
                self.final_dict["songs"]["mood"] = "positive"
            else:
                self.final_dict["songs"]["mood"] = "neutral"


    #use spotify to calculate a song's energy
    def calculate_song_energy(self):
        for song in self.spotify_dictionary:
            energy = self.spotify_dictionary["audio_feature"][0]["energy"]
            danceability = self.spotify_dictionary["audio_feature"][0]["danceability"]
            # loudness = self.spotify_dictionary["audio_feature"][0]["loudness"]
            # tempo = self.spotify_dictionary["audio_feature"][0]["tempo"]

            total_energy = (energy * 0.8) + (danceability * 0.3)
            self.final_dict[""]


    def calculate_playlist_mood(self):
        pass


    #calculate sentiment in sections; add to final_dict
    def calculate_percentages(self):
        pass



if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    print(analyzer.calculate_compound_sentiment("She'd take the world off my shoulders.\
                                        If it was ever hard to move.\
                                        She'd turn the rain to a rainbow\
                                        When I was living in the blue\
                                        Why then, if she's so perfect\
                                        Do I still wish that it was you?\
                                        Perfect don't mean that it's workin'\
                                        So what can I do? (Ooh)"))

    analyzer.receive_dictionary({
                                "audio_features": [
                                    {
                                    "acousticness": 0.00242,
                                    "analysis_url": "https://api.spotify.com/v1/audio-analysis/2takcwOaAZWiXQijPHIx7B",
                                    "danceability": 0.585,
                                    "duration_ms": 237040,
                                    "energy": 0.842,
                                    "id": "2takcwOaAZWiXQijPHIx7B",
                                    "instrumentalness": 0.00686,
                                    "key": 9,
                                    "liveness": 0.0866,
                                    "loudness": -5.883,
                                    "mode": 0,
                                    "speechiness": 0.0556,
                                    "tempo": 118.211,
                                    "time_signature": 4,
                                    "track_href": "https://api.spotify.com/v1/tracks/2takcwOaAZWiXQijPHIx7B",
                                    "type": "audio_features",
                                    "uri": "spotify:track:2takcwOaAZWiXQijPHIx7B",
                                    "valence": 0.428
                                    }
                                ]
                                })
    
    # print(analyzer.calculate_valence())