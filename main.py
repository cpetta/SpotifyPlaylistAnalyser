import sys

from commandline_ui import CommandLineUI
from playlist import Playlist
from auth import Auth
from artist import Artist
from album import Album
from settings import Settings

settings = Settings()

ARTIST_REC_LIMIT = 10
GENRE_LIMIT = 5

# Get playlist URL from user
UI = CommandLineUI()

# Authenticate with Spotify and get a token
auth = Auth(settings)

# Get playlist information.
playlist = Playlist(auth, UI.url)

# Print playlist Genres
print(f"\nTop {GENRE_LIMIT} Playlist Genres\n")
i:int = 0
for genre in playlist.genres.keys():
	if i > GENRE_LIMIT:
		break
	i += 1
	print(f"{playlist.genres[genre]} - {genre}")

# for album in playlist.albums.values():
# 	for genre in album.genres:
# 		print(genre)

# sys.exit()

# Create list of recomended artists
print("\nNumber of artists in playlist", len(playlist.artists), "\n")

print(f"\nTop {ARTIST_REC_LIMIT} Recommended Artists\n")

recomended_artists_list:dict[str, Artist] = {};

for artist in playlist.artists.values():
	recomended_artists_list = artist.get_related_artists(auth, recomended_artists_list)

	for recomended_artist in recomended_artists_list.values():
		id:str = recomended_artist.id
		recomended_artists_list[id] = recomended_artist

ranked_recomended_artists = sorted(recomended_artists_list.values())


# Print results
i:int = 0
for recomended_artist in ranked_recomended_artists:
	if i >= ARTIST_REC_LIMIT:
		break
	i += 1
	print(f"\n Recomendation {i}: {recomended_artist}")