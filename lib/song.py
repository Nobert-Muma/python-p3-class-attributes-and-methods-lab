class Song:
    count=0
    artists=[]
    genres=[]
    genre_count={}
    artist_count={}
    def __init__(self, name, artist, genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count+=increment
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre]=1
        else:
            cls.genre_count[genre]+=1
        print(cls.genre_count)
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist]=1
        else:
            cls.artist_count[artist]+=1
# Creating the first song
song1 = Song("Savage", "21 Savage", "Rap")

# Print class-level attributes
print("Count of songs:", Song.count)
print("Genres:", Song.genres)
print("Artists:", Song.artists)
print("Genre count:", Song.genre_count)
print("Artist count:", Song.artist_count)

# Creating multiple songs
song2 = Song("Blinding Lights", "The Weeknd", "Pop")
song3 = Song("Rockstar", "Post Malone", "Rap")
song4 = Song("Someone Like You", "Adele", "Pop")

# Print class-level attributes
print("Count of songs:", Song.count)
print("Genres:", Song.genres)
print("Artists:", Song.artists)
print("Genre count:", Song.genre_count)
print("Artist count:", Song.artist_count)

# Creating songs with duplicate genres and artists
song5 = Song("Circles", "Post Malone", "Pop")
song6 = Song("God's Plan", "Drake", "Rap")
song7 = Song("Hello", "Adele", "Pop")

# Print class-level attributes
print("Count of songs:", Song.count)
print("Genres:", Song.genres)
print("Artists:", Song.artists)
print("Genre count:", Song.genre_count)
print("Artist count:", Song.artist_count)


# Creating songs with empty or unusual values
song8 = Song("", "", "")          # Empty values
song9 = Song("Unique Song", "Unique Artist", "Unique Genre")

# Print class-level attributes
print("Count of songs:", Song.count)
print("Genres:", Song.genres)
print("Artists:", Song.artists)
print("Genre count:", Song.genre_count)
print("Artist count:", Song.artist_count)
