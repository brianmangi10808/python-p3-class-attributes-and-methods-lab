#!/usr/bin/env python3

class Song:
    count = 0
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

if __name__ == "__main__":
    # Instantiating some songs to show how the class works
    song1 = Song("99 Problems", "Jay Z", "Rap")
    song2 = Song("Halo", "Beyonce", "Pop")
    song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
    song4 = Song("Out of Touch", "Hall and Oates", "Pop")

    # Outputs to demonstrate functionality
    print(f"Total number of songs: {Song.count}")
    print(f"Genres count: {Song.genre_count}")
    print(f"Artists count: {Song.artist_count}")
