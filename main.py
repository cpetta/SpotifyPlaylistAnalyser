from commandline_ui import CommandLineUI
from playlist import Playlist
from auth import Auth
from artist import Artist
from settings import Settings
from tqdm import tqdm


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
print('------------------------------')
print(f"Top {GENRE_LIMIT} Playlist Genres")
print('------------------------------')

i:int = 0
for genre in playlist.genres.keys():
	if i > GENRE_LIMIT:
		break
	i += 1
	print(f"{playlist.genres[genre]} - {genre}")


# Create list of recomended artists
print("\nNumber of artists in playlist:", len(playlist.artists), "\n")

print('------------------------------')
print(f"Top {ARTIST_REC_LIMIT} Recommended Artists")
print('------------------------------')

recomended_artists_list:dict[str, Artist] = {};

for artist in tqdm(playlist.artists.values()):
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
	print(f"\nRecomendation {i}: {recomended_artist}")