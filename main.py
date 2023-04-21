from commandline_ui import CommandLineUI
from spotify_playlist import Playlist
from spotify_auth import Auth
from artist import Artist
from settings import Settings

settings = Settings()


UI = CommandLineUI()
auth = Auth(settings)
playlist = Playlist(auth, UI.url)


# Debug
i:int = 0
limit:int = 50
print("Number of artists ", len(playlist.artists))
recomended_artists_list:dict[str, Artist] = {};
for artist in playlist.artists.values():
	i += 1
	if(i > limit):
		break
	recomended_artists_list = artist.get_related_artists(auth, recomended_artists_list)

	for recomended_artist in recomended_artists_list.values():
		id:str = recomended_artist.id
		recomended_artists_list[id] = recomended_artist

for recomended_artist in recomended_artists_list.values():
	print(recomended_artist)