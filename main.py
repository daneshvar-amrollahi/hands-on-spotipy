import time
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

if __name__ == '__main__':
    scope = "user-library-read user-read-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    webbrowser.open("https://open.spotify.com/playlist/4LuLZqAtpf4To5rPCz8p5a?si=8a53d3cf69704282&nd=1")

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
            ███████ ███████ ██      ███████
            ██      ██      ██      ██
            █████   █████   ██      ███████
            ██      ██      ██           ██
            ███████ ███████ ███████ ███████

            """)

        current_song = sp.currently_playing()

        song_name = current_song['item']['name']
        artist_name = current_song['item']['album']['artists'][0]['name']
        print(f"Playing {song_name} from {artist_name}...")

        progress = current_song['progress_ms']
        duration = current_song['item']['duration_ms']

        blocks = (int)((progress/duration) * 100)

        print("+", end = "")
        for i in range(98):
            print("-", end = "")
        print("+")

        print("|", end = "")
        for i in range(blocks - 1):
            print("*", end = "")
        for i in range(99 - blocks):
            print(" ", end = "")
        print("|")

        print("+", end="")
        for i in range(98):
            print("-", end = "")
        print("+")

        time.sleep(3)

