from commandline_ui import CommandLineUI
from spotify_playlist import Playlist
from spotify_auth import Auth
from settings import Settings

settings = Settings()

auth = Auth(settings)
UI = CommandLineUI()
playlist = Playlist(auth, UI.url)

i:int = 0
limit:int = 50
print("Number of artists ", len(playlist.artists))
for artist_id in playlist.artists.keys():
    i += 1
    if(i > limit):
        break
    print(artist_id)

# print("playlist ID", playlist.id)