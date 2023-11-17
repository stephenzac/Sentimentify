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
        self.num_songs = 0


    """SETTING INFORMATION"""

    def receive_information(self, dictionary: dict) -> None:
        self.num_songs += 1

        songName = dictionary["songName"]
        self.lyrics[songName] = dictionary["lyrics"]
        self.spotify_dictionary[songName] = dictionary["spotifyDictionary"]

        self.final_dict["songs"][songName] = {}
        self.song_mood_stats[songName] = [-1, -1, -1, -1]



    """GETTERS"""

    def get_final_dictionary(self) -> dict:
        return self.final_dict



    """INDIVIDUAL SONGS"""

    #add valence to song_stats in -1 to 1 scale
    def calculate_valence(self) -> None:
        for song in self.spotify_dictionary:
            self.song_mood_stats[song][0] = self.spotify_dictionary[song]["valence"]


    #calculate sentiment analysis of a song's lyrics
    def calculate_compound_sentiment(self) -> None:

        for song in self.lyrics:
            self.song_mood_stats[song][1] = self.vader.polarity_scores(self.lyrics[song])['compound'] * 0.5 + 0.5


    #use compound sentiment and valence to calculate total mood
    def calculate_song_mood(self) -> None:
        for song in self.song_mood_stats:
            if self.song_mood_stats[song][1] == -1:
                mood = self.song_mood_stats[song][0]
            else:
                mood = (self.song_mood_stats[song][0] * 0.7) + (self.song_mood_stats[song][1] * 0.3)

            if mood <= 0.33:
                self.final_dict["songs"][song]["mood"] = "Negative"
            elif mood >= 0.66:
                self.final_dict["songs"][song]["mood"] = "Positive"
            else:
                self.final_dict["songs"][song]["mood"] = "Neutral"

            self.song_mood_stats[song][2] = mood


    #use spotify to calculate a song's energy
    def calculate_song_energy(self) -> None:
        for song in self.spotify_dictionary:
            energy = self.spotify_dictionary[song]["energy"]
            danceability = self.spotify_dictionary[song]["danceability"]

            total_energy = (energy * 0.8) + (danceability * 0.3)
            if total_energy <= 0.33:
                self.final_dict["songs"][song]["energy"] = "Low"
            elif total_energy >= 0.66:
                self.final_dict["songs"][song]["energy"] = "High"
            else:
                self.final_dict["songs"][song]["energy"] = "Medium"

            self.song_mood_stats[song][3] = total_energy



    """PLAYLIST TOTALS"""

    #calculates the mood of the overall playlist
    def calculate_playlist_mood(self) -> None:
        playlistMood = 0
        for song in self.song_mood_stats:
            playlistMood += self.song_mood_stats[song][2]

        if playlistMood / self.num_songs <= 0.33:
            self.final_dict["playlist"][self.playlistName]["mood"] = "Negative"
        elif playlistMood / self.num_songs >= 0.66:
            self.final_dict["playlist"][self.playlistName]["mood"] = "Positive"
        else:
            self.final_dict["playlist"][self.playlistName]["mood"] = "Neutral"


    #calculates the energy of the overall playlist
    def calculate_playlist_energy(self) -> None:
        playlistEnergy = 0
        for song in self.song_mood_stats:
            playlistEnergy += self.song_mood_stats[song][3]

        if playlistEnergy / self.num_songs <= 0.33:
            self.final_dict["playlist"][self.playlistName]["energy"] = "Low"
        elif playlistEnergy / self.num_songs >= 0.66:
            self.final_dict["playlist"][self.playlistName]["energy"] = "High"
        else:
            self.final_dict["playlist"][self.playlistName]["energy"] = "Medium"


    #calculate percentage of each energy and mood; adds percentages to final_dict
    def calculate_percentages(self) -> None:
        negMood = 0
        neuMood = 0
        posMood = 0
        highEnergy = 0
        medEnergy = 0
        lowEnergy = 0

        for song in self.final_dict["songs"]:
            if self.final_dict["songs"][song]["mood"] == "Positive":
                posMood +=1
            elif self.final_dict["songs"][song]["mood"] == "Neutral":
                neuMood += 1
            else:
                negMood += 1
            
            if self.final_dict["songs"][song]["energy"] == "High":
                highEnergy += 1
            elif self.final_dict["songs"][song]["energy"] == "Medium":
                medEnergy += 1
            else:
                lowEnergy += 1
        
        self.final_dict["moodPercentages"]["Positive"] = f"{posMood / self.num_songs * 100:.2f}%"
        self.final_dict["moodPercentages"]["Neutral"] = f"{neuMood / self.num_songs * 100:.2f}%"
        self.final_dict["moodPercentages"]["Negative"] = f"{negMood / self.num_songs * 100:.2f}%"
        self.final_dict["energyPercentages"]["High"] = f"{highEnergy / self.num_songs * 100:.2f}%"
        self.final_dict["energyPercentages"]["Medium"] = f"{medEnergy / self.num_songs * 100:.2f}%"
        self.final_dict["energyPercentages"]["Low"] = f"{lowEnergy / self.num_songs * 100:.2f}%"
