import webbrowser

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

if __name__ == '__main__':

    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    print("""
███████ ███████ ██      ███████ 
██      ██      ██      ██      
█████   █████   ██      ███████ 
██      ██      ██           ██ 
███████ ███████ ███████ ███████ 
                                                   
""")

    print("******************************************************")
    print("Welcome to Eels-Bot!")
    print("******************************************************")

    print("What do you want to listen to from this lovely band?")
    print("1 - Spotify's Eels Essentials")
    print("2 - Daneshvar's Picks")
    print("Just enter your number:", end = " ")

    q = int(input())

    if q == 1:
        webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DZ06evO24NfX2?si=0b690e33647f444e&nd=1")
    if q == 2:
        webbrowser.open("https://open.spotify.com/playlist/4LuLZqAtpf4To5rPCz8p5a?si=530714c88dd34eca&nd=1")

    print("Cool new features coming soon!")