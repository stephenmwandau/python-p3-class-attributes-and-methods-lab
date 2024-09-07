class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__ (self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        return cls.count

    @classmethod
    def add_to_genres(cls, genre):
        if genre in cls.genres:
            print("Genre is already in the list!!")
        else:
            cls.genres.append(genre)
            print([genre for genre in cls.genres])


    @classmethod
    def add_to_artists(cls, artist):
        if artist in cls.artists:
            print("Artist is already in the list!!")
        else:
            cls.artists.append(artist)
            print([artist for artist in cls.artists])

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
        print(f"{cls.genre_count}")

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
        print(f"{cls.artist_count}")

ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
halo = Song("Halo", "Beyonce", "Pop")
smells_like_teen_spirit = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
state_of_mind = Song("Empire State of Mind", "Jay-Z", "Rap")