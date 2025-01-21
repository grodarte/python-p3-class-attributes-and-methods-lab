class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.update_list(self.genres, genre)
        self.update_list(self.artists, artist)
        self.update_count(self.genre_count, genre)
        self.update_count(self.artist_count, artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def update_list(cls, lst, item):
        if item not in lst:
            lst.append(item)

    @classmethod
    def update_count(cls, count_dict, item):
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1