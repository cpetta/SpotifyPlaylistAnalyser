from commandline_ui import CommandLineUI
from spotify_playlist import Playlist
from spotify_auth import Auth
from artist import Artist
from settings import Settings

settings = Settings()

ARTIST_REC_LIMIT = 10
GENRE_LIMIT = 5

UI = CommandLineUI()
auth = Auth(settings)
playlist = Playlist(auth, UI.url)

print("Number of artists ", len(playlist.artists))
recomended_artists_list:dict[str, Artist] = {};
for artist in playlist.artists.values():
	recomended_artists_list = artist.get_related_artists(auth, recomended_artists_list)

	for recomended_artist in recomended_artists_list.values():
		id:str = recomended_artist.id
		recomended_artists_list[id] = recomended_artist

ranked_recomended_artists = sorted(recomended_artists_list.values())

for recomended_artist in ranked_recomended_artists:
	print(recomended_artist)