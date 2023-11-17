from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:

    def __init__(self, playlistName: str):
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
                "positive": "10.00",
                "neutral": "50.00",
                "negative": "40.00"
            },
            "energyPercentages": {
                "high": "40",
                "medium": "10",
                "low": "50"
            }
        }

        lyrics is a dictionary with the song title as the key and a string as the item {song_title : "lyrics"}
        dictionary is the received Spotify dictionary
        vader is the sentiment analyzer object
        song_mood_stats is a dictionary {song_title : [valence, vader_sentiment, finalMood, finalEnergy]}
        """

        self.lyrics = {}
        self.spotify_dictionary = {}
        self.vader = SentimentIntensityAnalyzer()
        self.playlistName = playlistName
        self.final_dict = {"playlist" : {playlistName : {}}, "songs" : {}, "moodPercentages" : {}, "energyPercentages" : {}}


        self.song_mood_stats = {}


    """SETTING INFORMATION"""

    #receive lyrics
    def receive_lyrics(self, lyrics: dict) -> None:
        self.lyrics = lyrics


    #receive Spotify dictionary
    def receive_dictionary(self, dictionary: dict) -> None:
        self.spotify_dictionary = dictionary

        for song in self.spotify_dictionary:
            #initializes final_dict
            self.final_dict["songs"][song] = {}

            #intializes song_mood_stats
            self.song_mood_stats[song] = [-1, -1, -1, -1]



    """GETTERS"""

    def get_final_dictionary(self) -> dict:
        return self.final_dict



    """INDIVIDUAL SONGS"""

    #add valence to song_stats in -1 to 1 scale
    def calculate_valence(self) -> None:
        for song in self.spotify_dictionary:
            self.song_mood_stats[song][0] = self.spotify_dictionary[song]["audio_features"][0]["valence"]


    #calculate sentiment analysis of a song's lyrics
    #Do it line by line?
    def calculate_compound_sentiment(self) -> None:

        for song in self.lyrics:
            self.song_mood_stats[song][1] = self.vader.polarity_scores(self.lyrics[song])['compound'] * 0.5 + 0.5

        #or
        # for song in self.lyrics:
        #     sentiment = 0
        #     numLines = 0
        #     lines = self.lyrics[song].split('.')

        #     for line in lines:
        #         sentiment += self.vader.polarity_scores(line)["compound"]
        #         numLines += 1
            
        #     self.song_mood_stats[song][1] = sentiment / numLines


    #use compound sentiment and valence to calculate total mood
    def calculate_song_mood(self) -> None:
        for song in self.song_mood_stats:
            if self.song_mood_stats[song][1] == -1:
                mood = self.song_mood_stats[song][0]
            else:
                mood = (self.song_mood_stats[song][0] * 0.7) + (self.song_mood_stats[song][1] * 0.3)

            if mood <= 0.33:
                self.final_dict["songs"][song]["mood"] = "negative"
            elif mood >= 0.66:
                self.final_dict["songs"][song]["mood"] = "positive"
            else:
                self.final_dict["songs"][song]["mood"] = "neutral"

            self.song_mood_stats[song][2] = mood


    #use spotify to calculate a song's energy
    def calculate_song_energy(self) -> None:
        for song in self.spotify_dictionary:
            energy = self.spotify_dictionary[song]["audio_features"][0]["energy"]
            danceability = self.spotify_dictionary[song]["audio_features"][0]["danceability"]
            # loudness = self.spotify_dictionary["audio_features"][0]["loudness"]
            # tempo = self.spotify_dictionary["audio_features"][0]["tempo"]

            total_energy = (energy * 0.8) + (danceability * 0.3)
            if total_energy <= 0.33:
                self.final_dict["songs"][song]["energy"] = "low"
            elif total_energy >= 0.66:
                self.final_dict["songs"][song]["energy"] = "high"
            else:
                self.final_dict["songs"][song]["energy"] = "medium"

            self.song_mood_stats[song][3] = total_energy



    """PLAYLIST TOTALS"""

    #calculates the mood of the overall playlist
    def calculate_playlist_mood(self) -> None:
        playlistMood = 0
        for song in self.song_mood_stats:
            playlistMood += self.song_mood_stats[song][2]

        if playlistMood <= 0.33:
            self.final_dict["playlist"][self.playlistName]["mood"] = "negative"
        elif playlistMood >= 0.66:
            self.final_dict["playlist"][self.playlistName]["mood"] = "positive"
        else:
            self.final_dict["playlist"][self.playlistName]["mood"] = "neutral"


    #calculates the energy of the overall playlist
    def calculate_playlist_energy(self) -> None:
        playlistEnergy = 0
        for song in self.song_mood_stats:
            playlistEnergy += self.song_mood_stats[song][3]

        if playlistEnergy <= 0.33:
            self.final_dict["playlist"][self.playlistName]["energy"] = "low"
        elif playlistEnergy >= 0.66:
            self.final_dict["playlist"][self.playlistName]["energy"] = "high"
        else:
            self.final_dict["playlist"][self.playlistName]["energy"] = "medium"


    #calculate percentage of each energy and mood; adds percentages to final_dict
    def calculate_percentages(self) -> None:
        negMood = 0
        neuMood = 0
        posMood = 0
        highEnergy = 0
        medEnergy = 0
        lowEnergy = 0

        for song in self.final_dict["songs"]:
            if self.final_dict["songs"][song]["mood"] == "positive":
                posMood +=1
            elif self.final_dict["songs"][song]["mood"] == "neutral":
                neuMood += 1
            else:
                negMood += 1
            
            if self.final_dict["songs"][song]["energy"] == "high":
                highEnergy += 1
            elif self.final_dict["songs"][song]["energy"] == "medium":
                medEnergy += 1
            else:
                lowEnergy += 1
        
        numSongs = len(self.final_dict["songs"])
        self.final_dict["moodPercentages"]["positive"] = f"{posMood / numSongs * 100:.2f}%"
        self.final_dict["moodPercentages"]["neutral"] = f"{neuMood / numSongs * 100:.2f}%"
        self.final_dict["moodPercentages"]["negative"] = f"{negMood / numSongs * 100:.2f}%"
        self.final_dict["energyPercentages"]["high"] = f"{highEnergy / numSongs * 100:.2f}%"
        self.final_dict["energyPercentages"]["medium"] = f"{medEnergy / numSongs * 100:.2f}%"
        self.final_dict["energyPercentages"]["low"] = f"{lowEnergy / numSongs * 100:.2f}%"



if __name__ == "__main__":
    pass
    # analyzer = SentimentAnalyzer("Hello")

    # analyzer.receive_dictionary({"Stacy's Mom" : {
    #                                 "audio_features": [
    #                                     {
    #                                     "danceability": 0.652,
    #                                     "energy": 0.945,
    #                                     "valence": 0.823
    #                                     }
    #                                 ]},
    #                                 "Glimpse of Us" : {
    #                                     "audio_features": [
    #                                     {
    #                                     "danceability": 0.506,
    #                                     "energy": 0.106,
    #                                     "valence": 0.089
    #                                     }
    #                                 ]}
    #                             })
    
    # analyzer.receive_lyrics({"Stacy's Mom" : "Stacy, can I come over after school? (After school)\
    #                                             We can hang around by the pool (Hang by the pool)\
    #                                             Did your mom get back from her business trip? (Business trip)\
    #                                             Is she there, or is she trying to give me the slip? (Give me the slip)\
    #                                             You know, I'm not the little boy that I used to be\
    #                                             I'm all grown up now, baby, can't you see?\
    #                                             Stacy's mom has got it going on\
    #                                             She's all I want and I've waited for so long\
    #                                             Stacy, can't you see? You're just not the girl for me\
    #                                             I know it might be wrong, but I'm in love with Stacy's mom",
    #                         "Glimpse of Us" : "'Cause sometimes, I look in her eyes\
    #                                             And that's where I find a glimpse of us\
    #                                             And I try to fall for her touch\
    #                                             But I'm thinkin' of the way it was\
    #                                             Said I'm fine and said I moved on\
    #                                             I'm only here passing time in her arms\
    #                                             Hopin' I'll find a glimpse of us\
    #                                             Tell me he savors your glory\
    #                                             Does he laugh the way I did?\
    #                                             Is this a part of your story?\
    #                                             One that I had never lived\
    #                                             Maybe one day, you'll feel lonely\
    #                                             And in his eyes, you'll get a glimpse\
    #                                             Maybe you'll start slippin' slowly and find me again"

    #                         })
    
    # analyzer.calculate_valence()
    # analyzer.calculate_compound_sentiment()
    # analyzer.calculate_song_mood()
    # analyzer.calculate_song_energy()
    # analyzer.calculate_playlist_mood()
    # analyzer.calculate_playlist_energy()
    # analyzer.calculate_percentages()
    # print(analyzer.get_final_dictionary())