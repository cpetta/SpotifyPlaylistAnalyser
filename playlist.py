import re
import spotify_api

from auth import Auth
from artist import Artist
from album import Album


class Playlist:
	def __init__(self, auth:Auth, url:str):
		self.url:str = url
		self.id:str = self.get_id()
		self.data:dict = spotify_api.get_playlist(auth, self.id)
		self.albums:dict[str, Album] = self.get_playlist_albums(auth)
		self.artists:dict[str, Artist] = self.get_playlist_artists()
		self.genres:list = self.get_playlist_genres(auth)

	def get_id(self) -> str:
		if not self.check_url(self.url):
			return ""

		slugs:list[str] = self.url.split("/")
		slugs_last:int = len(slugs) - 1
		id_slug:str = slugs.pop(slugs_last)
		id:str = id_slug.split("?")[0]
		return id


	def get_playlist_artists(self) -> dict[str, Artist]:
		artists:dict[str, Artist] = {}

		if(self.id == ""):
			return artists
		
		tracks = self.data['tracks']['items']

		for track in tracks:
			for trackArtist in track['track']['artists']:
				id:str = trackArtist['id']
				name:str = trackArtist['name']

				artist:Artist = Artist(id, name)
				artists[id] = artist
		return artists


	def get_playlist_albums(self, auth) -> dict[str, Album]:
		albums:dict[str, Album] = {}

		if(self.id == ""):
			return albums
		
		tracks = self.data['tracks']['items']

		for track in tracks:
			for trackAlbumID in track['track']['album'].values():
				if trackAlbumID not in albums:
					albums[trackAlbumID] = Album(auth, trackAlbumID)
		return albums


	def get_playlist_genres(self, auth) -> list:
		# get each Artist Genre
		artist_ids = []

		for artist in self.artists.values():
			artist_ids.append(artist.id)

		genres = spotify_api.get_several_artists_genres(auth, artist_ids)

		return genres

	@staticmethod
	def check_url(url:str) -> bool:
		pattern = "https:\/\/open\.spotify\.com\/playlist\/"
		is_spotify_playlist = re.match(pattern, url)

		if(is_spotify_playlist):
			return True
		else:
			return False

