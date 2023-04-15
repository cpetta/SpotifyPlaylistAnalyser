from commandline_ui import CommandLineUI
from spotify_playlist import Playlist
from spotify_auth import Auth

auth = Auth()
print(auth)
UI = CommandLineUI()
playlist = Playlist(UI)

print(playlist.id)