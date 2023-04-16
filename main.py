from commandline_ui import CommandLineUI
from spotify_playlist import Playlist
from spotify_auth import Auth
from settings import Settings

settings = Settings()

auth = Auth(settings)
UI = CommandLineUI()
playlist = Playlist(auth, UI.url)

for artist in playlist.artists.values():
    print(artist)

# print("playlist ID", playlist.id)